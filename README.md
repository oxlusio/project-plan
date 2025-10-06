# Cost of Living Index Dashboard 

ENG220 Project Repository regarding the Cost of Living Index analysis and visualization.

## Project Overview

This project presents an interactive Streamlit web application that analyzes and visualizes cost of living data across different countries worldwide. The application provides comprehensive insights into various economic factors that affect the cost of living, including housing costs, groceries, restaurant prices, and local purchasing power.

## Features

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

## Team Members

**ENG220 Project Team:**
-

*Note: Please update the team member names and roles according to your actual team composition.*

##  Dependencies

- **streamlit>=1.28.0** - Web application framework
- **pandas>=2.0.0** - Data manipulation and analysis
- **plotly>=5.15.0** - Interactive visualizations
- **numpy>=1.24.0** - Numerical computing

## Usage

1. **Country Selection**: Use the sidebar to select specific countries for comparison
2. **Index Selection**: Choose different cost of living indices to analyze
3. **Interactive Charts**: Hover over charts for detailed information
4. **World Map**: Explore global cost of living patterns
5. **Data Download**: Export data for further analysis

## Data Sources

Currently, the application uses sample data for demonstration purposes. In a production environment, data would be sourced from:
- [Numbeo](https://www.numbeo.com/) - Cost of Living Database
- [World Bank Open Data](https://data.worldbank.org/)
- [OECD Data](https://data.oecd.org/)

## Deployed Application

🔗 **Live Demo**: https://project-plan-f7snzypxbnrnnz4v2y8rwv.streamlit.app/
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

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
