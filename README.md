### Sentiment Analyses of Linganore-Oakdale-Urbana Area Redistricting

Author: Meng Chen

---------------------------
### About

Southeastern communities of Frederick County has been growing steadfast due to newly approved development projects in this area. Local schools have been growing over their designed capacity for years. Particularly, in Urbana area, a huge working force will join the local community as a new biopharmaceutical manufacturing facility is being established by [Kite Pharma](https://www.kitepharma.com) and a hotel and restaurant chain will be build in next two years. There is a urgent need to redistrict local schools based on changing feeding patterns.

Based on the message of the Board of Education, Frederick County, the redistricting roots on the inequal development of the local communities ([here for detials](https://www.fcps.org/capital-program/linganore-oakdale-urbana-area-redistricting-study).) However, the redistricting study stired local communities because of concerns of the student development, property price, community integrity, and etc.

This project primarily focuses on sentiments after the second-round proposal for redistricting LOU. The analyses were based on public avaliable datasets (survey results and current districts) provided by CropperGIS Inc that is contractor carries out the LOU redistricting study and Frederick County, respectively.

---------------------------

### Data origination

The original survey data can be download as [PDF files](https://www.fcps.org/capital-program/lou-meetings).

The shapefile that can be download at Frederick County [website](https://www.frederickcountymd.gov/5969/Download-GIS-Data).

---------------------------

### redistrict Module
This module includes three newly developed classes, SentiAnalysis(), shape2json(), and MapVisualization(). Each class have been specifically
developed to analyze the public assessible data.

##### Class SentiAnalysis()
The class can take either a string or a text file as input to calculate sentiment scores. It cleans the text before the analyses. The SentiWordNet 3.0 has been used to score the sentiments of the words. Three different weighting schemes have been used. In addition, the proportion of positive, negative, and neutural feedbacks are generated as well raw scores of individual word in the data.

**Input would like this**:
'Welcome to our new house.' or 'comments_school_redistricting.txt'
**Out put would like this**:

##### Class shape2json()

##### Class MapVisualization()


If you have any questions, please contact me at meng.chen03@gmail.com.
