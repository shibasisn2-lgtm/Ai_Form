import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ask Your CSV",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ask Your CSV")
st.markdown("Upload your data and ask questions in plain English!")


# Sidebar for file upload
with st.sidebar:
    st.header("📁 Data Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            
            # Create data summary for token optimization
            st.session_state.data_summary = {
                "shape": df.shape,
                "columns": df.columns.tolist(),
                "dtypes": df.dtypes.to_dict(),
                "sample": df.head(3).to_dict(),
                "stats": df.describe().to_dict() if not df.empty else {}
            }
            
            st.success(f"✅ Loaded {df.shape[0]} rows × {df.shape[1]} columns")
            
            # Data preview
            with st.expander("Preview Data"):
                st.dataframe(df.head())
                
            # Basic stats
            with st.expander("Data Summary"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Rows", df.shape[0])
                    st.metric("Total Columns", df.shape[1])
                with col2:
                    st.metric("Memory Usage", f"{df.memory_usage().sum() / 1024:.1f} KB")
                    st.metric("Missing Values", df.isnull().sum().sum())
                    
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            st.info("Please make sure your file is a valid CSV format.")
    else:
        st.info("👆 Upload a CSV file to start analyzing!")
    

# Chat input
st.chat_input('Ask a question about your data')

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "df" not in st.session_state:
    st.session_state.df = None
if "data_summary" not in st.session_state:
    st.session_state.data_summary = None

st.title("📊 Ask Your CSV")
st.markdown("Upload your data and ask questions in plain English!")