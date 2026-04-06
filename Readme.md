# 📊 Vrinda Store Sales Dashboard

> **Freelance Data Analytics Project** delivering end-to-end business intelligence solutions for Vrinda E-Commerce Store.

An interactive sales analytics dashboard built using Python (Plotly/Dash), Tableau, and Tableau Prep to analyze e-commerce transaction data and deliver actionable business insights for Vrinda Store.

## 💼 Project Background

This was a **freelance data analytics project** where I worked with Vrinda Store to analyze their sales performance and build comprehensive dashboards for data-driven decision making.

This project demonstrates a complete data analytics workflow — from data acquisition and cleaning to exploratory analysis, static visualization, interactive dashboards, and business intelligence reporting. The analysis examines sales performance across channels, geographies, payment modes, and customer segments to identify growth opportunities and operational improvements.

### Key Responsibilities

- 📊 Structured and cleaned raw e-commerce sales dataset from Vrinda Store
- 🔍 Performed exploratory data analysis to identify business trends and patterns
- 🔄 Built a scalable ETL pipeline using Tableau Prep for data transformation
- 📈 Developed static visualizations for presentation and reporting
- 💻 Built an interactive Python web dashboard using Plotly and Dash
- 📊 Created a professional Tableau dashboard for executive stakeholders
- 📝 Delivered actionable business recommendations based on data insights

### 🎯 Business Questions

- How do sales vary across different months and quarters?
- Which states generate the highest revenue?
- What is the distribution of customers by gender and age group?
- How does order fulfillment perform?
- Which sales channels contribute the most to revenue?
- What patterns exist in customer purchases by demographics?
- Are there any visible sales trends and seasonal patterns?

### 📦 Dataset

- **Source**: Vrinda Store Sales Data
- **Link**: [Vrinda Store Sales Dataset](https://www.kaggle.com/datasets/amitkumar209/vrinda-store-sales-data)
- **Records**: 31,047 transactions across multiple channels and states
- **Time Period**: Full Year 2022
- **Key Attributes**: Order ID, Date, Amount, Quantity, Channel, Gender, Age, State, Status

### 🔗 Live Demo

- **🌟 Tableau Public Dashboard** (Live & Interactive): [Explore on Tableau Public](https://public.tableau.com/app/profile/amitkr209/viz/VrindaStoreDashboard/VrindaDashboard) ← **Click to interact with the live dashboard**
  
- **Interactive Python Dashboard**: [Watch the Dashboard in Action](/Images/Vrinda%20Sales%20Interactive%20Dashboard.gif)

- **Tableau Desktop**: [View Dashboard Preview](/Images/Tableau%20Dashboard.gif)

- **Static Dashboard**: [Executive Summary](/Images/Vrinda%20Store%20Static%20Dashboard.png)

## 🚀 Project Workflow

This project follows a complete data analysis pipeline:

**Step-by-Step Process:**

1. **Data Ingestion & Cleaning**
   - Loaded Vrinda Store sales dataset (31K+ transactions)
   - Standardized gender values (M/W → Men/Women)
   - Converted data types (text quantities to numeric)
   - Parsed dates and extracted temporal features
   - Implemented kagglehub API for automated data acquisition

2. **Data Transformation with Tableau Prep**
   - Built scalable ETL pipeline (Vinda_Sales_Data_Prep_Flow.tfl)
   - Gender column standardization
   - Quantity column type conversion
   - Date parsing with month & quarter extraction
   - Age group binning (Young <30 / Adult 30-49 / Senior 50+)
   - Unnecessary column removal
   - Cleaned dataset export for downstream use

3. **Exploratory Data Analysis**
   - Calculated key metrics (revenue, profit, quantity, AOV)
   - Analyzed trends across time, geography, and channels
   - Identified top customers, states, and payment patterns
   - Customer demographics segmentation

4. **Static Dashboard**
   - Created publication-ready visualizations using Matplotlib and Seaborn
   - 6-panel dashboard with KPIs, monthly trends, and distributions
   - High-level overview for executive reporting

5. **Interactive Dashboard**
   - Built web-based dashboard using Plotly and Dash
   - Implemented dynamic quarter-based filtering
   - Created responsive layouts with callback functions
   - Real-time metric updates

6. **Tableau Dashboard**
   - Designed professional BI dashboard with Tableau Desktop
   - Implemented interactive filters and parameters
   - Geographic and temporal analysis capabilities
   - Drill-down and cross-filtering features

## 📁 Project Structure

```
Vrinda-Store-Sales-Dashboard/
│
├── Vrinda_Store_Sales_Analysis.ipynb        # Complete data analysis & static dashboard
├── vrinda_dashboard.py                      # Interactive Dash application
├── Vinda_Sales_Data_Prep_Flow.tfl          # Tableau Prep ETL pipeline
├── Vrinda_Store_Sales_Dashboard.twb         # Tableau Desktop workbook
├── Vrinda_Store_Static_Dashboard.png        # Static dashboard screenshot
├── Tableau_Dashboard.gif                    # Tableau dashboard animation
├── Tableau_Flow_Image.png                   # Prep pipeline visualization
├── Vrinda_Sales_Interactive_Dashboard.gif   # Interactive dashboard animation
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation
```

## 🛠️ Tools & Technologies

### Programming

- Python

### Libraries

- Pandas → Data cleaning & analysis  
- NumPy → Data processing  
- Matplotlib → Static visualizations  
- Seaborn → Advanced visualizations  
- Plotly → Interactive charts  
- Dash → Web-based interactive dashboard  

### BI & Data Tools

- Tableau Desktop → Business intelligence dashboard
- Tableau Prep → ETL data pipeline

### Other Tools

- Jupyter Notebook  
- VS Code  
- Git & GitHub  

## 📊 Dashboards

### 1️⃣ Tableau Dashboard (Live on Tableau Public)

Professional business intelligence dashboard with multi-dimensional filtering and drill-down capabilities.

**🌟 [ACCESS LIVE DASHBOARD ON TABLEAU PUBLIC](https://public.tableau.com/app/profile/amitkr209/viz/VrindaStoreDashboard/VrindaDashboard)** ← Click here to explore the interactive dashboard online!

![Tableau Dashboard](/Images/Tableau%20Dashboard.gif)

**Key Features:**

- Interactive filters and parameters
- Real-time KPI cards (Revenue, Orders, Quantity, AOV, Customers)
- Monthly revenue and order trends
- Geographic revenue distribution by state
- Order status analysis (Delivered, Returned, Cancelled, Refunded)
- Customer segmentation by gender and age
- Channel performance analysis
- Fully responsive and shareable via Tableau Public link

### 2️⃣ Python Interactive Dashboard (Plotly + Dash)

Web-based interactive dashboard with dynamic filtering and responsive design.

![Python Dashboard](/Images/Vrinda%20Sales%20Interactive%20Dashboard.gif)

**Key Features:**

- **Dynamic Filters**: Quarter-based filtering (Q1-Q4, All)
- **Real-time Updates**: All visualizations update based on filter selections
- **KPI Indicators**: 
  - Total Revenue: ₹21.2M
  - Total Orders: 31K
  - Quantity Sold: 31.2K units
  - Average Order Value: ₹682.1
  - Unique Customers: 28.4K
- **Interactive Charts**:
  - Monthly revenue and order trends (dual-axis chart)
  - Revenue distribution by gender (pie chart)
  - Order status breakdown (pie chart)
  - Top 5 revenue states (bar chart)
  - Channel order distribution (bar chart)
  - Age group & gender cross-tabulation (grouped bar chart)

### 3️⃣ Static Dashboard

High-level overview dashboard for executive reporting and presentations.

![Static Dashboard](/Images/Vrinda%20Store%20Static%20Dashboard.png)

**Key Components:**

- Monthly revenue and order trends
- Revenue distribution by gender
- Top revenue states (top 5)
- Order status distribution
- Channel order distribution
- Age group and gender analysis

## 📦 Project Deliverables & Releases

This project is organized into distinct professional releases to provide tailored solutions for both executive decision-makers and technical analysts.

### 📊 [Tableau Business Intelligence Dashboard (v1.0.0-tableau)](https://public.tableau.com/app/profile/amitkumar209/viz/VrindaStoreSalesDashboard/Dashboard1)

* **Target Audience**: Business owners and executive stakeholders focused on high-level performance.
* **Live Access**: Available on [Tableau Public](https://public.tableau.com/app/profile/amitkr209/viz/VrindaStoreDashboard/VrindaDashboard) for instant online access (no installation required)
* **Core Metrics**: Immediate visibility into Total Revenue (₹21.2M), Total Orders (31K), and Quantity (31.2K units).
* **Visual Intelligence**: Geographic revenue distribution across states and temporal trend analysis.
* **Advanced Analytics**: Interactive filters, parameters, and drill-down capabilities for deep analysis.
* **Deliverables**: 
  - 🌐 Live Tableau Public dashboard (shareable link)
  - 📥 Tableau Desktop workbook (.twb file) for local exploration
* **Accessibility**: Share dashboard link with stakeholders without requiring Tableau licenses

### 🌐 [Interactive Python Web Analytics (v2.0.0-python)]()

* **Target Audience**: Data analysts and developers requiring a scalable, code-driven analytics environment.
* **Technical Stack**: Fully reactive web application built with **Dash**, **Plotly**, and **Pandas**.
* **Data Automation**: Programmatic acquisition using the `kagglehub` API for seamless data updates.
* **Dynamic Interactivity**: Advanced Dash callbacks enabling real-time filtering by Quarter across all 11 visuals.
* **Technical Value**: Demonstrates a complete Python-based data pipeline and visualization architecture.

### 🔄 [Tableau Prep ETL Pipeline (v1.0.0-prep)]

* **Target Audience**: Data engineers and ETL specialists focused on scalable data transformation.
* **Purpose**: Transparent, reusable data cleaning and transformation pipeline.
* **Features**: Gender standardization, type conversion, date parsing, age binning, column cleanup.
* **Value**: Scalable approach to data preparation with documented transformation logic.

## 📈 Key Business Insights 🔍

### 1. **Women are the dominant customer segment with strong revenue contribution**

  - Women generate **64% of revenue** (₹13.6M) vs Men **36%** (₹7.6M)
   - This pattern is consistent across all age groups
   - Female dominance across Young (70%), Adult (68%), and Senior (70%) segments
   - Strategic marketing should prioritize women-centric campaigns

### 2. **Sales show strong seasonality with Q4 declining performance**

   - **March** is the peak month with **₹1.93M** revenue and **2,819** orders
   - **November** is the weakest month with **₹1.62M** revenue (~16% decline from peak)
   - Clear Q1 strength followed by gradual decline through the year
   - Revenue drops by **16%** from peak (March) to low (November)

### 3. **Geographic concentration presents both strength and opportunity**

   - Top 5 states (Maharashtra, Karnataka, Uttar Pradesh, Telangana, Tamil Nadu) = **52.6%** of revenue
   - **Maharashtra** leads with **₹2.99M** (14.1% of total)
   - **Karnataka** contributes **₹2.65M** (12.5% of total)
   - **Uttar Pradesh** generates **₹2.10M** (9.9% of total)
   - High geographic concentration indicates need for expansion into underperforming states

### 4. **E-commerce channels show clear performance hierarchy**

   - **Amazon** dominates with **35.5%** of total orders
   - **Myntra** (fashion-focused) captures **23.4%** of orders
   - **Flipkart** (general e-commerce) contributes **21.6%** of orders
   - Top 3 channels = **80.5%** of total revenue
   - Secondary channels (Ajio, Nalli, Meesho, Others) have significant growth potential

### 5. **Adult segment (30-49 years) drives core business with Young segment untapped**

   - **Adult customers** account for **50.6%** of total orders
   - **Young segment** (18-29) = **30.3%** (growth potential)
   - **Senior segment** (50+) = **19.1%** (loyalty opportunity)
   - Adult segment is revenue backbone; Young segment shows demographic growth potential

### 6. **Strong fulfillment performance with 7.7% churn as improvement opportunity**

   - **Delivered orders**: 92.3% (28,641 out of 31,047)
   - **Returned orders**: 3.4% (1,045 orders)
   - **Cancelled orders**: 2.7% (837 orders)
   - **Refunded orders**: 1.7% (517 orders)
   - Combined churn of 7.7% represents **₹1.63M in potential revenue loss**

## 💡 Business Recommendations & Action Plan

### 🎯 Customer Targeting Strategy

**Primary Target Segment:**

- Women aged 30-49 (Adult segment)
- Generates 50.6% of orders with highest revenue per customer
- Consistent purchasing behavior across channels

**Secondary Target Segment:**

- Young women aged 18-29
- Growing demographic with mobile-first shopping behavior
- Opportunity for customer acquisition and lifetime value building

**Tertiary Target Segment:**

- Senior women (50+)
- Loyal customer base with stable purchasing patterns
- Opportunity for premium/loyalty offerings

### 📍 Geographic Strategy

#### 🔝 High-Priority States (Maintain & Scale)

| State | Revenue | Share | Strategy |
|-------|---------|-------|----------|
| Maharashtra | ₹2.99M | 14.1% | Maintain leadership; premium product focus |
| Karnataka | ₹2.65M | 12.5% | Defend position; expand product depth |
| Uttar Pradesh | ₹2.10M | 9.9% | Grow market share; localized marketing |

#### 📈 Growth Opportunity States (Expand & Invest)

- **Telangana** & **Tamil Nadu** - Top 5 states with room to scale
- **Underperforming states** - Launch geo-targeted campaigns to expand reach
- **Regional strategy** - Use local language content and region-specific offers

### 🛒 Channel Strategy

#### 💎 Top Performing Channels (Invest More)

- **Amazon** (35.5% share) - Highest volume platform; increase marketing spend
- **Myntra** (23.4% share) - Fashion-focused; ideal for women's product category
- **Flipkart** (21.6% share) - Broad reach; maintain competitive presence

#### 🚀 Secondary Channels (Test & Scale)

- **Ajio** (6.2%), **Nalli** (4.8%), **Meesho** (4.5%)
- Potential for growth with targeted promotions
- Lower saturation provides testing opportunity

### 📊 Summary Action Plan

| Priority | Action | Expected Impact | Timeline |
|----------|--------|-----------------|----------|
| 🔴 High | Target women 30-49 via Amazon/Myntra/Flipkart with segment-specific creatives | +15-20% revenue growth | Q2-Q3 |
| 🔴 High | Launch Q4 re-engagement campaigns to reduce seasonal dip | Stabilize Q4 revenue by +10% | Q3-Q4 |
| 🟡 Medium | Expand geo-targeting to underperforming states (Telangana, Tamil Nadu, others) | +8-12% geographic growth | Q2-Q4 |
| 🟡 Medium | Reduce churn rate from 7.7% to <5% through improved descriptions and tracking | Recover ₹500K+ in revenue | Ongoing |
| 🟢 Low | Test secondary channels (Ajio, Meesho) with targeted bundle offers | Channel diversification; +5% revenue | Q3-Q4 |

### 📣 Tactical Recommendations

#### 🗓️ Seasonal Campaigns

- **Q1 Maximization**: Double marketing investment in January-March to capitalize on peak demand
- **Q4 Recovery**: Launch aggressive campaigns in September-October to counter November-December slowdown
- **Seasonal Offers**: Monthly promotional themes aligned with festivals and shopping seasons
- **Target**: Reduce 16% peak-to-low revenue gap to <10%

#### 💰 Customer Retention & AOV

- **Improve Product Information**: Reduce 3.4% return rate through better descriptions and sizing guides
- **Simplified Returns**: Offer exchanges instead of full returns to maintain customer lifetime value
- **Bundling Strategy**: Cross-sell related products to increase average order value from ₹682.1
- **Loyalty Program**: Repeat customer coupons and threshold-based offers for AOV lift

#### 📱 Digital Marketing

- **Geo-targeted Ads**: Priority states (MH, KA, UP) via Amazon Ads and platform-specific campaigns
- **Demographic Targeting**: Women 30-49 with lifestyle and product-specific creatives
- **Regional Customization**: Use regional languages for underperforming states
- **Channel-Specific Campaigns**: Tailored messaging for Amazon/Myntra/Flipkart based on platform audiences

#### 🔄 Operational Excellence

- **Order Tracking**: Proactive notifications to reduce 2.7% cancellation rate
- **Fulfillment Quality**: Maintain 92.3% delivery rate; target 95%+ fulfillment
- **Payment Options**: Maintain COD for conversion while promoting prepaid (faster fulfillment)
- **Quality Assurance**: Weekly monitoring of churn metrics and corrective actions

## 🚀 Getting Started
 
### Prerequisites

```bash
Python 3.12+
pip (Python package manager)
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/amitkumar209/vrinda-store-sales-dashboard.git

cd vrinda-store-sales-dashboard
```

2. **Install dependencies**

```bash
python -m pip install -r requirements.txt
```

3. **Download the dataset**
   - The script automatically downloads data from Kaggle using KaggleHub
   - Dataset link: [Vrinda Store Sales Data on Kaggle](https://www.kaggle.com/datasets/amitkumar209/vrinda-store-sales-data)
   - Manual download: Download the CSV file from the Kaggle link above

### Running the Dashboard

**Option 1: 🌟 View Live on Tableau Public (No Installation Required)**

🎯 **Fastest way to explore the dashboard:**

```
👉 [Click here to open the live Tableau Public dashboard](https://public.tableau.com/app/profile/amitkr209/viz/VrindaStoreDashboard/VrindaDashboard)
```

**Benefits:**

- No installation or setup required
- Fully interactive dashboard online
- Shareable link for stakeholders
- Real-time data exploration
- Works on any device with internet

---

**Option 2: Run the Interactive Dash App (Locally)**

```bash
python vrinda_dashboard.py
```

Then open your browser and navigate to: `http://127.0.0.1:8050/`

---

**Option 3: Explore the Jupyter Notebook**

```bash
jupyter notebook Vrinda_Store_Sales_Analysis.ipynb
```

---

**Option 4: View Tableau Dashboard (Desktop Version)**

```bash
# Open in Tableau Desktop
Vrinda_Store_Sales_Dashboard.twb
```

## 📚 Key Learnings & Project Scope

### 💼 Freelancing Project Deliverables

- ✅ **Client Requirements**: Sales performance analysis and interactive dashboards
- ✅ **Data Cleaning**: Comprehensive data preparation and standardization
- ✅ **ETL Pipeline**: Scalable Tableau Prep workflow for data transformation
- ✅ **Multi-format Delivery**: Python dashboards, Tableau reports, and static visualizations
- ✅ **Business Insights**: Actionable recommendations for revenue optimization
- ✅ **Documentation**: Complete project documentation and code comments

### Technical Skills Demonstrated

- ✅ End-to-end data pipeline development
- ✅ Data cleaning and transformation with Pandas
- ✅ Statistical analysis and metric calculation
- ✅ Static visualization best practices (Matplotlib/Seaborn)
- ✅ Interactive dashboard development (Plotly/Dash)
- ✅ Web application development with Python
- ✅ Business intelligence reporting (Tableau)
- ✅ ETL pipeline design (Tableau Prep)
- ✅ API integration (Kaggle)

### Business Skills Demonstrated

- ✅ KPI definition and tracking
- ✅ Trend analysis and seasonality identification
- ✅ Customer segmentation and demographics
- ✅ Geographic analysis and market concentration
- ✅ Channel performance optimization
- ✅ Strategic recommendation development
- ✅ Data-driven decision support

## 🎓 Use Cases & Portfolio Value

This project is ideal for showcasing:

- **Freelance Data Analytics Experience**: End-to-end client project delivery
- **Data Analyst Portfolio**: Complete analytics capabilities from data cleaning to insights
- **Business Intelligence Role**: Demonstrates multi-platform BI dashboard development
- **E-commerce Analytics**: Shows domain expertise in retail/e-commerce metrics
- **Dashboard Developer Position**: Proves ability to build interactive, client-ready visualizations
- **ETL Pipeline Development**: Demonstrates data engineering and transformation skills

## 🌐 Cloud Deployment & Sharing

### Tableau Public Dashboard

This project's Tableau dashboard has been published to **Tableau Public** for instant online access and easy sharing.

**🌟 [Access the Live Dashboard Here](https://public.tableau.com/app/profile/amitkr209/viz/VrindaStoreDashboard/VrindaDashboard)**

## 🎬 Conclusion

This Vrinda Store Sales Dashboard project represents a **complete data analytics lifecycle** — from raw business requirements to actionable insights and interactive visualizations. As a freelance engagement, it showcases not just technical proficiency, but also the ability to:

### 💡 Key Achievements

**📊 Technical Excellence:**

- Built three different dashboard platforms (Static, Interactive Web, Tableau) from a single dataset
- Implemented scalable ETL pipeline using Tableau Prep for data transformation
- Demonstrated mastery across the entire Python data science stack
- Created production-ready, client-facing dashboards with professional polish

**🚀 Process & Deliverables:**

- Cleaned and standardized raw e-commerce sales data with comprehensive preprocessing
- Completed exploratory data analysis identifying 6 major business insights
- Built multi-platform dashboards tailored to different stakeholder needs
- Provided strategic recommendations backed by data-driven analysis
- Delivered actionable business plans with specific impact projections

**💼 Business Value:**

- Identified ₹1.63M in potential revenue recovery through churn reduction
- Quantified 15-20% revenue growth opportunity through targeted campaigns
- Pinpointed geographic expansion opportunities in underperforming states
- Provided channel strategy recommendations for increased market share

This project serves as a foundation for building similar analytics solutions across various e-commerce and retail domains, demonstrating adaptability and scalable analytical thinking.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📊 Project Statistics

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.6+-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-teal.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.11+-red.svg)
![Dash](https://img.shields.io/badge/Dash-2.7+-purple.svg)
![Tableau](https://img.shields.io/badge/Tableau-Latest-yellow.svg)

[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-blue?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/amitkumar209/vrinda-store-sales-data)

![License](https://img.shields.io/badge/License-MIT-orange.svg)

---

<div align="center">
  ⭐ Found this project useful? Show your support by starring the repository!
</div>