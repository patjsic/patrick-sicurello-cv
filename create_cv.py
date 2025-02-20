from fpdf import FPDF

class CustomPDF(FPDF):
    """Custom PDF style chart for FPDF object. Currently hardcoding dejavusans.
    """
    def header(self):
        """Header includes personal information and is divided by a bottom line with 5 spacing.
        """
        # Use the registered DejaVu font for Unicode
        self.set_font("DejaVu", "", 16)
        self.cell(0, 10, "Patrick Sicurello", ln=1, align="C")

        self.set_font("DejaVu", "", 11)
        self.cell(0, 6, "3100 Fallscliff Road, Baltimore, MD, 21211", ln=1, align="C")
        self.cell(0, 6, "patsicurello@gmail.com | Tel: (510) 305-8493 | GitHub: github.com/patjsic", ln=1, align="C")

        # Small spacing after header
        self.ln(2)

        # Draw a horizontal line
        self.set_draw_color(0, 0, 0)    # black line
        self.set_line_width(0.5)
        line_start = 10
        line_end = self.w - 10
        y = self.get_y()
        self.line(line_start, y, line_end, y)
        self.ln(5)

    def section_title(self, title: str, top_spacing: float=10.0, bottom_spacing: float=10.0):
        """Section title with variable top and bottom spacing.

        Args:
            title (str): Title of section
            top_spacing (float, optional): Amount of whitespace above section title. Defaults to 10.0.
            bottom_spacing (float, optional): Amount of whitespace below section title. Defaults to 10.0.
        """
        # Add top spacing
        self.ln(top_spacing)
        
        self.set_font("DejaVu", "B", 12)
        self.cell(0, 6, title.upper(), ln=1)

        self.set_draw_color(0, 0, 0)
        self.set_line_width(0.2)
        line_start = 10
        line_end = self.w - 10
        y = self.get_y() + 1
        self.line(line_start, y, line_end, y)
        
        # Add space after the line
        self.ln(bottom_spacing)

    def sub_heading(self, position: str, dates_location: str=""):
        """Prints the job title/institution as a bold heading, then optional italic subheading (location/dates).

        Args:
            position (str): Job title/institution for heading
            dates_location (str, optional): Location/dates for subheading. Defaults to "".
        """
        self.set_font("DejaVu", "B", 11)
        self.cell(0, 5, position, ln=1)

        if dates_location:
            self.set_font("DejaVu", "I", 10)
            self.cell(0, 5, dates_location, ln=1)

        self.ln(2)

    def bullet_point(self, text: str):
        """Prints a bullet point (Unicode bullet '•'), then wraps text in multiple lines if necessary.

        Args:
            text (str): Text to go in bulleted list
        """
        # Unicode bullet
        bullet_char = "•"
        self.set_font("DejaVu", "", 11)
        self.cell(5, 5, bullet_char, 0, 0)
        self.multi_cell(0, 5, text)

def create_unicode_cv():
    pdf = CustomPDF()

    # Register the DejaVu font for Unicode support -- assumes tff files in same directory
    pdf.add_font("DejaVu", "",   "fonts/DejaVuSans.ttf",         uni=True)  # Regular
    pdf.add_font("DejaVu", "B",  "fonts/DejaVuSans-Bold.ttf",    uni=True)  # Bold
    pdf.add_font("DejaVu", "I",  "fonts/DejaVuSans-Oblique.ttf", uni=True)  # Italic
    pdf.add_page()

    #
    # EDUCATION
    #
    pdf.section_title("Education")

    pdf.sub_heading("Johns Hopkins University", "Baltimore, MD | 08/2023 – Present")
    pdf.set_font("DejaVu", "", 11)
    pdf.multi_cell(0, 5, "M.A. in Applied Mathematics")

    pdf.ln(3)
    pdf.sub_heading("University of California, Berkeley", "Berkeley, CA | 08/2016 – 12/2020")
    pdf.multi_cell(0, 5, "B.A. in Physics and Applied Mathematics")

    pdf.ln(3)
    pdf.sub_heading("University of California, San Diego", "Remote | 09/2021 – 03/2022")
    pdf.multi_cell(0, 5, "Certificate in Machine Learning")

    #
    # RESEARCH INTERESTS
    #
    pdf.section_title("Research Interests")
    interests = [
        "Scientific Machine Learning (SciML), Geometric Deep Learning",
        "Remote Sensing, Geospatial AI, Uncertainty Quantification",
        "Physics-Informed Neural Networks (PINNs)",
        "Out-of-Distribution (OOD) Detection in Multivariate Time Series"
        "Data Science for Climate, Additive Manufacturing"
    ]
    for item in interests:
        pdf.bullet_point(item)

    #
    # PROFESSIONAL EXPERIENCE
    #
    pdf.section_title("Professional Experience")

    # JHUAPL
    pdf.sub_heading("Machine Learning Researcher at Johns Hopkins University Applied Physics Laboratory",
                    "Laurel, MD | 07/2022 – Present")
    jhu_exps = [
        "Develop deep learning models for global GHG emissions estimation using GIS and OSM data as part of Climate TRACE.",
        "Implement Physics-Informed Neural Networks (PINNs) to predict sea ice drift vectors in dynamic environments.",
        "Fine-tune geospatial foundation models (GeoFM) for GIS image segmentation and classification.",
        "Perform uncertainty quantification for calibration of additive manufacturing processes.",
        "Research novel methods for detecting out-of-distribution (OOD) data in multivariate time series.",
        "Routinely write grant proposals and pitch research ideas (NASA Cryosphere, NOAA, U.S. Navy).",
        "Work presented at American Meteorological Society Conference, AGU, and COP29."
    ]
    for exp in jhu_exps:
        pdf.bullet_point(exp)

    pdf.ln(3)

    # Hedgehog
    pdf.sub_heading("Machine Learning Engineer at Hedgehog AI",
                    "Palo Alto, CA | 10/2021 – 07/2022")
    hedgehog_exps = [
        "Trained and deployed NLP models for named-entity recognition on pet insurance claims.",
        "Supported client teams in model implementation and troubleshooting deployment issues.",
        "Served as primary client liaison to ensure smooth model integration and adoption."
    ]
    for exp in hedgehog_exps:
        pdf.bullet_point(exp)

    pdf.ln(3)

    # Freelance
    pdf.sub_heading("Freelance Developer", "Berkeley, CA | 10/2020 – 11/2021")
    freelance_exps = [
        "Developed Jupyter Notebook plugins to improve data science workflows for remote clients.",
        "Designed and implemented autograders for the University of Maryland Global Campus Data Science coursework.",
        "Optimized data pipelines for downstream analytics and automation."
    ]
    for exp in freelance_exps:
        pdf.bullet_point(exp)

    #
    # PUBLICATIONS & DOCUMENTATION
    #
    pdf.section_title("Publications & Technical Documentation")

    # Posters
    pdf.set_font("DejaVu", "B", 11)
    pdf.cell(0, 5, "Conference Presentations & Posters", ln=1)
    pdf.ln(2)

    pdf.set_font("DejaVu", "", 11)
    pdf.multi_cell(0, 5,
        "Sicurello, P. Physics-Informed Machine Learning for Characterization of Arctic Sea Ice.\n"
        " - Presented at AGU Fall Meeting 2023\n"
        " - DOI: 10.22541/essopenarchive.1264263.v1"
    )
    pdf.ln(3)

    # Tech docs
    pdf.set_font("DejaVu", "B", 11)
    pdf.cell(0, 5, "Technical Documentation", ln=1)
    pdf.ln(2)

    pdf.set_font("DejaVu", "", 11)
    tech_docs = [
        ("Climate TRACE Wastewater Treatment Plant Emissions Estimation Methodology\n"
         " - GitHub: climatetracecoalition/methodology-documents"),
        ("Climate TRACE Global Road Transportation Emissions Methodology\n"
         " - GitHub: climatetracecoalition/methodology-documents")
    ]
    for doc in tech_docs:
        pdf.bullet_point(doc)

    #
    # TECH SKILLS
    #
    pdf.section_title("Technical Skills")
    tech_skills = [
        "Programming: Python (PyTorch, TensorFlow, Scikit-learn), Java, PySpark, SQL, R, MATLAB",
        "Machine Learning: Deep Learning, Bayesian Optimization, Probabilistic Graphical Models",
        "Geospatial AI: QGIS, OpenStreetMap (OSM), GeoPandas, Raster Data Processing",
        "MLOps & Deployment: Docker, Kubernetes, AWS, Azure, MLFlow, Weights & Biases (wandb)",
        "Data Science & Visualization: NumPy, Pandas, Matplotlib, Seaborn"
    ]
    for skill in tech_skills:
        pdf.bullet_point(skill)

    #
    # SELECTED PROJECTS
    #
    pdf.section_title("Selected Projects")
    projects = [
        ("Variational Autoencoder (VAE) for Out-of-Distribution Detection\n"
         " - Developed a beta-VAE model to detect anomalous time-series data and performed statistical tests."),
        ("Geospatial Deep Learning for Environmental Monitoring\n"
         " - Applied GeoFM models to identify wastewater treatment ponds using geospatial embeddings."),
        ("Best-Subset Selection for Regression Analysis\n"
         " - Implemented best-subset selection, AIC, BIC, and cross-validation to analyze data.")
    ]
    for prj in projects:
        pdf.bullet_point(prj)

    #
    # AWARDS & GRANTS
    #
    pdf.section_title("Awards & Grants")
    awards = [
        "NASA Cryosphere Research Grant (Co-PI, 2024)",
        "NOAA Research Funding for Geospatial AI Applications (2023)",
        "JHU Applied Physics Lab IRAD Award (2023)"
    ]
    for award in awards:
        pdf.bullet_point(award)

    #
    # PROFESSIONAL MEMBERSHIPS
    #
    pdf.section_title("Professional Memberships")
    memberships = [
        "American Geophysical Union (AGU)",
        "American Meteorological Society (AMS)",
    ]
    for membership in memberships:
        pdf.bullet_point(membership)

    #
    # Export to PDF
    #
    pdf_name = "Patrick_Sicurello_CV.pdf"
    pdf.output(pdf_name)
    print(f"CV successfully created: {pdf_name}")

if __name__ == "__main__":
    create_unicode_cv()

