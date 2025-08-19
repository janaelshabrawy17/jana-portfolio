import streamlit as st
import base64

st.set_page_config(page_title="Jana's Portfolio", layout="wide")

# -------- Sidebar Navigation --------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to:", ["About Me", "Projects", "Certifications", "Contact"])

# -------- About Me --------
if page == "About Me":
    st.title("👋 Hello, I'm Jana")
    st.subheader("📊 Data Analyst | 🐍 Python Developer | 💡 Creative Thinker")

    st.write("""
    Welcome to my portfolio website. I’m passionate about solving problems with data and building Python applications.
    Here you'll find some of the projects I've worked on, my skills, and how to contact me.
    """)

    st.header("🔍 About Me")
    st.write("""
    - 🎓 Computer Science Student at Zewail City  
    - 💼 Interested in Data Analysis and Web Development  
    - 📚 Learning Python, OOP, and Data Acquisition  
    """)

    st.header("🛠️ Skills")
    st.markdown("""
    - **Programming:** Python, C++, HTML, Streamlit  
    - **Data Tools:** Pandas, NumPy, Matplotlib  
    - **Other:** APIs, GitHub, Problem-Solving  
    """)

# -------- Projects --------
elif page == "Projects":
    st.title("📁 Projects")

    st.subheader("📊 eBay Price Analyzer")
    st.write("Scrapes and visualizes eBay data using BeautifulSoup and Streamlit.")
    st.markdown("[🔗 View on GitHub](https://github.com/janaelshabrawy17)")

    st.subheader("🧠 AI Course Registration System")
    st.write("University course system using C++ OOP.")

    st.subheader("🏥 Health Care App")
    st.write("Hospital health app using Python & Tkinter.")

    st.subheader("📝 To-Do List")
    st.write("A simple To-Do List app built with Python.")
    st.markdown("[🔗 View on GitHub](https://github.com/janaelshabrawy17/To-do-list)")
# -------- Certifications --------
elif page == "Certifications":
    st.title("🎓 Certifications")
    st.markdown("✅ Directions Program with EFE-Egypt")

    # PDF Viewer
    def display_pdf(file_path):
        import base64
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    # Use your uploaded certificate file
    display_pdf("Jana El-Shabrawy (1).pdf")

    # Download button
    with open("Jana El-Shabrawy (1).pdf", "rb") as file:
        st.download_button(
            label="⬇️ Download My Certificate (PDF)",
            data=file,
            file_name="Jana_El-Shabrawy_Certificate.pdf",
            mime="application/pdf"
        )

elif page == "Contact":
    st.title("📬 Contact Me")
    st.markdown("""
    - 📧 Email: **s-jana.elshabrawy@zewailcity.edu.eg**  
    - 💼 [LinkedIn](https://www.linkedin.com/in/janamelshabrawy17)  
    - 💻 [GitHub](https://github.com/janaelshabrawy17)  
    """)
