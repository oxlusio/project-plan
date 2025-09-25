# Cost of Living Index Dashboard 💰

ENG220 Project Repository regarding the Cost of Living Index analysis and visualization.

## 🎯 Project Overview

This project presents an interactive Streamlit web application that analyzes and visualizes cost of living data across different countries worldwide. The application provides comprehensive insights into various economic factors that affect the cost of living, including housing costs, groceries, restaurant prices, and local purchasing power.

## ✨ Features

- **Interactive Dashboard**: Dynamic filtering and country selection
- **Multiple Visualizations**: Bar charts, world maps, and correlation matrices
- **Cost Indices Analysis**: 
  - Cost of Living Index
  - Rent Index
  - Groceries Index
  - Restaurant Price Index
  - Local Purchasing Power Index
- **Data Export**: Download functionality for datasets
- **Responsive Design**: Mobile-friendly interface
- **Real-time Updates**: Interactive charts with Plotly

## 👥 Team Members

**ENG220 Project Team:**
- **Team Lead**: [Your Name] - Data Analysis & Streamlit Development
- **Data Scientist**: [Team Member 2] - Statistical Analysis & Visualization
- **UI/UX Designer**: [Team Member 3] - Interface Design & User Experience
- **Quality Assurance**: [Team Member 4] - Testing & Documentation

*Note: Please update the team member names and roles according to your actual team composition.*

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/oxlusio/project-plan.git
   cd project-plan
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser:**
   The application will automatically open in your default browser at `http://localhost:8501`

## 📦 Dependencies

- **streamlit>=1.28.0** - Web application framework
- **pandas>=2.0.0** - Data manipulation and analysis
- **plotly>=5.15.0** - Interactive visualizations
- **numpy>=1.24.0** - Numerical computing

## 🖥️ Usage

1. **Country Selection**: Use the sidebar to select specific countries for comparison
2. **Index Selection**: Choose different cost of living indices to analyze
3. **Interactive Charts**: Hover over charts for detailed information
4. **World Map**: Explore global cost of living patterns
5. **Data Download**: Export data for further analysis

## 📊 Data Sources

Currently, the application uses sample data for demonstration purposes. In a production environment, data would be sourced from:
- [Numbeo](https://www.numbeo.com/) - Cost of Living Database
- [World Bank Open Data](https://data.worldbank.org/)
- [OECD Data](https://data.oecd.org/)

## 🌐 Deployed Application

🔗 **Live Demo**: [Add your deployed Streamlit app link here]

*Deploy your application using one of these platforms:*
- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [Heroku](https://heroku.com/)
- [Railway](https://railway.app/)
- [Render](https://render.com/)

### Deployment Instructions

#### Streamlit Community Cloud (Recommended)
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Deploy with one click!

#### Local Docker Deployment
```bash
# Create Dockerfile (if needed)
docker build -t cost-of-living-app .
docker run -p 8501:8501 cost-of-living-app
```

## 📁 Project Structure

```
project-plan/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore file
└── data/                # Data files (future enhancement)
```

## 🔮 Future Enhancements

- [ ] Real-time data integration from APIs
- [ ] Historical trend analysis
- [ ] Prediction models for cost trends
- [ ] Currency conversion features
- [ ] Detailed city-level analysis
- [ ] User authentication and personalized dashboards
- [ ] Mobile application development

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or support, please contact:
- **Project Repository**: [https://github.com/oxlusio/project-plan](https://github.com/oxlusio/project-plan)
- **Course**: ENG220 - Engineering Data Analysis
- **Academic Year**: 2024-2025

## 🙏 Acknowledgments

- Course instructors and teaching assistants
- Data providers and open-source community
- Streamlit team for the amazing framework
- All team members for their contributions

---

**Made with ❤️ by the ENG220 Project Team**