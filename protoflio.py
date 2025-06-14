import streamlit as st

st.set_page_config(page_title="Jana's Portfolio", layout="centered")

# ✅ Show both images


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
- Python, C++, HTML, Streamlit  
- Pandas, NumPy, Matplotlib  
- APIs  
""")

st.header("📁 Projects")
st.markdown("**📊 eBay Price Analyzer**  \nScrapes and visualizes eBay data using BeautifulSoup and Streamlit.")
st.markdown("**🧠 AI Course Registration System**  \nUniversity course system using C++ OOP.")
st.markdown("🏥 Health Care App  \nHospital health app using Python.")
st.header("🎓 Certifications")
st.markdown("""
- ✅ [Directions program with EFE-Egypt]
  
""")

# ✅ Show embedded PDF certificate (Jana El-Shabrawy.pdf)
st.subheader("📄 View Certificate")
import base64

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

display_pdf("Jana El-Shabrawy.pdf")

# ✅ Download button
with open("Jana El-Shabrawy.pdf", "rb") as file:
    st.download_button(
        label="⬇️ Download My Certificate (PDF)",
        data=file,
        file_name="Jana_El-Shabrawy_Certificate.pdf",
        mime="application/pdf"
    )

st.header("📬 Contact")
st.markdown("""
- 📧 Email: s-jana.elshabrawy@zewailcity.edu.eg  
- 💼 [LinkedIn](https://www.linkedin.com/in/janamelshabrawy17)  
- 💻 [GitHub](https://github.com/janaelshabrawy17)  
""")

