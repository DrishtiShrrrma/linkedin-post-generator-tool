import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def process_posts(raw_file_path, processed_file_path=None):
    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        enriched_posts = []

        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = {**post, **metadata}  # Merge original post with extracted metadata
            enriched_posts.append(post_with_metadata)

    # Get unified tags
    unified_tags = get_unified_tags(enriched_posts)
    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
        post['tags'] = list(new_tags)

    # Save the enriched posts to a new file
    with open(processed_file_path, mode="w", encoding="utf-8") as outfile:
        json.dump(enriched_posts, outfile, indent=4, ensure_ascii=False)


def extract_metadata(post_text):
    # Updated prompt based on your example JSON
    template = '''
    You are given a LinkedIn post. Extract the following information in JSON format:
    1. "line_count": The number of lines in the post.
    2. "language": The language of the post. The language should be either "English" or "Hinglish" (Hindi + English).
    3. "tags": A list of up to three tags relevant to the content of the post.

    Example:
    If the post is about "Bug Fixes in AI" or "Gradient Accumulation", appropriate tags might be "AI", "Bug Fixes", or "Efficiency".

    Here is the LinkedIn post:
    {post_text}
    '''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post_text": post_text})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Unable to parse the response for the post.")
    return res


def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    
    # Collect all tags from posts
    for post in posts_with_metadata:
        unique_tags.update(post.get('tags', []))

    unique_tags_list = ', '.join(unique_tags)

    # Updated prompt for unified tags
    template = '''I will provide a list of tags. Unify these tags according to the following rules:
    1. Combine similar tags into one unified tag. Examples:
       - "Bug Fixes", "Fixes" → "Bug Fixes".
       - "Networking", "Events" → "Networking".
       - "AI Report", "AI Trends" → "AI Report".
       - "Motivation", "Inspiration" → "Motivation".
    2. Use title case for all tags (e.g., "AI Report").
    3. Output the result as a JSON object where the keys are original tags and the values are unified tags.

    Here are the tags: 
    {tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": unique_tags_list})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Unable to parse the unified tags.")
    return res


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
