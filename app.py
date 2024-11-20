Hugging Face's logo
Hugging Face
Search models, datasets, users...
Models
Datasets
Spaces
Posts
Docs
Enterprise
Pricing



Spaces:

DrishtiSharma
/
linkedin-post-generator


like
0

App
Files
Community
Settings
linkedin-post-generator
/
app.py

DrishtiSharma's picture
DrishtiSharma
Update app.py
fed1cb1
verified
6 minutes ago
raw

Copy download link
history
blame
edit
delete

4.45 kB
import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import json

# Improved app with more functionality
def main():
    st.set_page_config(page_title="LinkedIn Post Generator", layout="wide")
    st.title("🚀 LinkedIn Post Generator")
    st.markdown(
        """
        **Create impactful LinkedIn posts effortlessly.**  
        Customize your post with advanced options, analyze generated content, and save your creations.
        """
    )

    # Sidebar for advanced options
    st.sidebar.title("🔧 Customization Options")
    st.sidebar.markdown("Use these settings to personalize your generated post.")

    fs = FewShotPosts()
    tags = fs.get_tags()

    # User input sections
    st.sidebar.subheader("Post Preferences")
    selected_tag = st.sidebar.selectbox("Topic (Tag):", options=tags)
    selected_length = st.sidebar.radio("Post Length:", ["Short", "Medium", "Long"])
    selected_language = st.sidebar.radio("Language:", ["English", "Hinglish"])
    selected_tone = st.sidebar.selectbox(
        "Tone/Style:", ["Motivational", "Professional", "Informal", "Neutral"]
    )
    custom_context = st.sidebar.text_area(
        "Additional Context (Optional):",
        placeholder="Provide extra details or a specific direction for your post...",
    )

    # History tracking
    if "generated_posts" not in st.session_state:
        st.session_state.generated_posts = []

    # Main content
    st.subheader("Generate Your LinkedIn Post")

    if st.button("Generate Post"):
        with st.spinner("Generating your post..."):
            try:
                # Generate post
                post = generate_post(selected_length, selected_language, selected_tag)

                # Add tone and context to the prompt dynamically
                if selected_tone:
                    post = f"**Tone**: {selected_tone}\n\n{post}"
                if custom_context:
                    post += f"\n\n**Context Added**: {custom_context}"

                # Save to session history
                st.session_state.generated_posts.append(post)

                st.success("Post generated successfully!")
                st.markdown("### Your LinkedIn Post:")
                st.write(post)

                # Post analysis
                st.markdown("### Post Analysis:")
                post_analysis(post)

            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Display session history
    if st.session_state.generated_posts:
        st.markdown("### Generated Posts History:")
        for i, history_post in enumerate(st.session_state.generated_posts):
            st.markdown(f"**Post {i + 1}:**")
            st.write(history_post)

    # Save and Download
    st.markdown("---")
    st.subheader("Save or Share Your Post")
    if st.session_state.generated_posts:
        if st.button("Download All Posts"):
            download_posts(st.session_state.generated_posts)
        if st.button("Clear History"):
            st.session_state.generated_posts = []
            st.info("History cleared!")

    # Footer
    st.markdown(
        """
        ---
        📝 *Powered by OpenAI's ChatGroq and LangChain.*  
        📧 For feedback, contact: [support@example.com](mailto:support@example.com)
        """
    )


def post_analysis(post):
    """Perform basic analysis of the generated post."""
    word_count = len(post.split())
    char_count = len(post)
    tone_keywords = {
        "Motivational": ["inspire", "achieve", "goal", "success"],
        "Professional": ["expertise", "career", "opportunity", "industry"],
        "Informal": ["hey", "cool", "fun", "awesome"],
    }

    st.write(f"**Word Count:** {word_count}")
    st.write(f"**Character Count:** {char_count}")

    # Detect tone based on keywords (simple heuristic)
    detected_tone = "Neutral"
    for tone, keywords in tone_keywords.items():
        if any(keyword in post.lower() for keyword in keywords):
            detected_tone = tone
            break

    st.write(f"**Detected Tone:** {detected_tone}")


def download_posts(posts):
    """Allow users to download their posts."""
    posts_json = json.dumps(posts, indent=4)
    st.download_button(
        label="📥 Download Posts",
        data=posts_json,
        file_name="generated_posts.json",
        mime="application/json",
    )


# Run the app
if __name__ == "__main__":
    main()

