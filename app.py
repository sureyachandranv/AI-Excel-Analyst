from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def create_pdf(summary,findings,recommendations):
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []
    content.append(Paragraph("AI Excel Analyst Report", styles['Title']))
    content.append(Paragraph(f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",styles['BodyText']))
    content.append(Spacer(1, 12))
    content.append(Spacer(1, 12))
    content.append(Paragraph("Executive Summary", styles['Heading2']))
    content.append(Paragraph(summary, styles['BodyText']))
    content.append(Spacer(1,12))
    content.append(Paragraph("Key Findings", styles["Heading2"]))
    for finding in findings:
        content.append(Paragraph(f"• {finding}", styles['BodyText']))
    content.append(Spacer(1,12))
    content.append(Paragraph("Recommendations", styles["Heading2"]))
    for recommendation in recommendations:
        content.append(Paragraph(f"• {recommendation}", styles['BodyText']))
    pdf.build(content)
    buffer.seek(0)
    return buffer
st.title("AI Excel Analyst")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    rows, cols = df.shape
    st.subheader("Dataset Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rows", rows)
    with col2:
        st.metric("Columns", cols)
    st.subheader("Data Types")
    st.write(df.dtypes)
    st.subheader("Summary Statistics")
    st.write(df.describe())
    st.subheader("Columns")
    st.dataframe(pd.DataFrame(df.columns, columns=["Column Names"]))
    st.subheader("Missing Values")
    st.write(df.isnull().sum())
    st.subheader("Missing Values by Column")
    missing = df.isnull().sum()
    fig, ax = plt.subplots()
    missing.plot(kind = 'bar', ax = ax)
    st.pyplot(fig)
    st.subheader("Numeric Columns")
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    st.dataframe(pd.DataFrame(numeric_cols,columns=["Numeric Columns"]))
    st.subheader("Column Visualization")
    selected_column = st.selectbox("Choose a Numeric Column", numeric_cols)
    fig, ax = plt.subplots()
    df[selected_column].hist(ax=ax)
    ax.set_title(f"Distribution of {selected_column}")
    st.pyplot(fig)
    st.subheader("Insights")

    mean_val = df[selected_column].mean()
    median_val = df[selected_column].median()

    st.write(f"Mean: {mean_val:.2f}")
    st.write(f"Median: {median_val:.2f}")

    if mean_val > median_val:
        st.success(
            "The distribution appears right-skewed. Some larger values may be pulling the average upward."
        )

    elif mean_val < median_val:
        st.success(
            "The distribution appears left-skewed. Some smaller values may be pulling the average downward."
        )

    else:
        st.success(
            "The distribution appears fairly symmetrical."
        )

    st.write("Unique Values: ", df[selected_column].nunique())
    st.subheader("Dataset Health Score")
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    col1,col2 = st.columns(2)
    health_score = ((total_cells - missing_cells)/total_cells)*100
    duplicates = df.duplicated().sum()
    with col1:
        st.metric("Health Score",f"{health_score:.1f}%")
    with col2:
        st.metric("Duplicate Rows", duplicates)
    st.subheader("Dataset Report")
    if health_score >= 95:
        st.success("Excellent Dataset Quality.")
    elif health_score >= 80:
        st.warning("Moderate Dataset Quality.")
    else:
        st.error("Poor Dataset Quality.")
    findings = []
    recommendations = []
    st.subheader("Key Findings")
    missing_data = df.isnull().sum()
    highest_missing_column = missing_data.idxmax()
    highest_missing_count = missing_data.max()
    highest_missing_percent = (highest_missing_count/len(df))*100
    finding1 = f"{highest_missing_column} contains {highest_missing_count} missing values ({highest_missing_percent:.1f}%)."
    findings.append(finding1)
    st.write(f"• {finding1}")
    if duplicates == 0:
        finding2 = "No duplicate records detected."
    else:
        finding2 = f"{duplicates} duplicate records detected."
    findings.append(finding2)
    st.write(f"• {finding2}")
    unique_counts = df.nunique()
    most_unique_column = unique_counts.idxmax()
    most_unique_count = unique_counts.max()
    if "id" in most_unique_column.lower():
        finding3 = (
            f"{most_unique_column} appears to be an identifier column "
            f"and may not be useful for predictive analysis."
        )
    else:
        finding3 = (
            f"{most_unique_column} has the highest number of unique values "
            f"({most_unique_count})."
        )

    findings.append(finding3)
    st.write(f"• {finding3}")
    if mean_val> median_val:
        finding4 = f"The {selected_column} shows a right-skewed distribution."
        findings.append(finding4)
        st.write(f"• {finding4}")
    elif mean_val < median_val:
        finding5 = f"The {selected_column} shows a left-skewed distribution."
        findings.append(finding5)
        st.write(f"• {finding5}")
    else:
        finding6 = f"The {selected_column} shows a fairly symmetrical distribution."
        findings.append(finding6)
        st.write(f"• {finding6}")
    st.subheader("Executive Summary")

    summary = f"""
    This dataset contains {df.shape[0]} records and {df.shape[1]} columns.
    The overall dataset health score is {health_score:.1f}%.
    The column with the highest missing values is {highest_missing_column}
    with {highest_missing_percent:.1f}% missing data.
    The selected column ({selected_column}) shows a
    {'right-skewed' if mean_val > median_val else 'left-skewed' if mean_val < median_val else 'symmetrical'}
    distribution.
    """

    st.info(summary)

    st.subheader("Column Type Detection")
    column_analysis = []
    for col in df.columns:
        if "id" in col.lower():
            column_analysis.append(f"{col} : Identifier Column")
        elif df[col].dtype == "object":
            column_analysis.append(f"{col} : Text/Categorical Column")
        else:
            column_analysis.append(f"{col} : Numeric Column")
    for item in column_analysis:
        st.write(item)
    
    st.subheader("Correlation Analysis")
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    corr_matrix = numeric_df.corr()
    st.dataframe(corr_matrix)

    st.subheader("Recommendations")

    if highest_missing_percent > 50:
        recommendation1 = f"Consider removing {highest_missing_column} because over 50% of its values are missing."
        recommendations.append(recommendation1)
        st.warning(f"• {recommendation1}")

        
    if duplicates == 0:
        recommendation2 = "No duplicate rows detected. Dataset is suitable for further analysis."
        recommendations.append(recommendation2)
        st.success(f"• {recommendation2}")

    if mean_val > median_val:
        recommendation3 = f"{selected_column} contains high-value outliers. Consider scaling or outlier treatment."
        recommendations.append(recommendation3)
        st.info(f"• {recommendation3}")
    
    if highest_missing_percent > 70:
        recommendation4 = (
            "Columns with over 70% missing values should be evaluated for removal."
        )

        recommendations.append(recommendation4)

        st.warning(f"• {recommendation4}")

    if "age" in selected_column.lower():
        recommendation5 = (
            "Missing Age values should be imputed before machine learning."
        )

        recommendations.append(recommendation5)
        st.info(f"• {recommendation5}")


    pdf_file = create_pdf(summary, findings, recommendations)
    st.download_button(label='Download PDF Report', data = pdf_file, file_name='Excel Report.pdf',mime='application/pdf')
