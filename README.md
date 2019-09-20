### Sentiment Analyses of Linganore-Oakdale-Urbana Area Redistricting (A two-week project)

@Meng Chen

---------------------------
### Introduction

Linganore-Oakdale-Urbana (LOU) Area is located in the southeastern area of the Frederick County of Maryland. During last ten years, the local communities have been transformed into well-maintained suburban residency for people who work in the Washington-Maryland area. Many professionals, such as administrative government employees or military personals chose to live in these neighborhoods, despite the distant transportation between their working place and home. Even some government facilities has located in this area. For an example, the Social Security Data Center is located next to the Park and Ride of the Exit 26 of Interstate-270 in the Urbana area. Recently, [Kite Pharma](https://www.kitepharma.com) is starting to build a pharmaceutical manufacturing facility here, and along its side, there will be a hotel and restaurant chain established in two years. Urbana area becomes the prime area for both business and residents.

These ongoing developments bring prosperity to the local communities. So does anxiety. For an example, the workforce brought by Kite Pharma has been estimated about 200-300 employees initially to 700-900 by its capacity. Such huge workforce will need hundreds of houses and/or apartments to acommendate their housing needs. Thus, the estate projects have been steadfastly developed in this area. More and more houses starts to show themselves off the landscape. However, only two new elementary schools have been added to the area, which cannot alleviate overcrowd situations in schools. It becomes clear that, without any additional government funding, the Board of Education of Frederick County has an urgent need to conduct school redistricting based on changing feeding patterns.

Starting in January, 2019, Frederick County has contracted with Cropper GIS Consulting to conduct the redistricting study, which is expected to completed by the end of the 2019. This study primarily focuses on attendance boundary and feeder patterns for two new schools that supposedly address the enrollment growth in this area and provides projections of the school enrollments in next 5-8 years. Based on the message of the Board of Education, the redistricting roots in their core belief that all students are entitled equally to respect, opportunity, and excellence ([here for details](https://www.fcps.org/capital-program/linganore-oakdale-urbana-area-redistricting-study).) However, after the Public Engagement Session in March, 2019, the proposed attendance boundary stirred the outrage from local communities based on analyses of the parents' feedbacks provided by the study. Such outrage seems to be alleviated by the new proposed attendance boundary at the Public Engagement Session of June, 2019 based on an initial assessment. Unfortunately, the quantitative assessment of parents' preferences were not provided to the public prior to the superintendent's recommendation that was presented on September 11, 2019.

This project primarily focuses on the sentiment and preferences of parents for new proposed options after Public Engagement Session in June, 2019. The parents' preferable options will be compared with the plan of the superintendent's recommendation to investigate whether Board of Education's choices are aligned with  parents' preferences and why. These will help board members understand the if parents support or oppose which option and parents recognize the education needs of the majority of the each community.

---------------------------

### Materials and Methods

---------------------------

#### Materials

---------------------------

The survey results after Public Engagement Session in June, 2019 for LOU Redistricting Study can be found in Frederick County Public Schools [website](https://www.fcps.org/capital-program/lou-meetings). The feedbacks are compiled in a PDF file, and represented as multiple tables in 209 pages. Prior to analyze the comments, the PDF file were converted to an excel file with three columns (school name, comments, and options). Additional cleaning proceedures will be detailed in the Methods.

The shapefiles of Frederick County School District have been downloaded at Frederick County [website](https://www.frederickcountymd.gov/5969/Download-GIS-Data). The shapefile contains the polygon data that splits the all Frederick County Public schools into different school district and were used to visualize the results. The shapefile was generated by ArcGIS under EPSG 2248. The EPSG was short for European Petroleum Survey Group but now known as the Geomatics Committee of the International Association of Oil and Gas Producers(OGP). 2248 is the EPSG spatial reference ID for Maryland. To project the Maryland to the world map, the coordinates in shapefile of Maryland were converted under the spatial reference ID EPSG 4326. See Methods for details.

---------------------------

#### Methods
___________________________



#### redistrict Module
This module includes three newly developed classes, _SentiAnalysis()_, _shape2json()_, and _MapVisualization()_. Each class have been specifically
developed to analyze the public accessible data of LOU Redistricting.

Class  | Description
------ | -----------
SentiAnalysis() | Analyze the sentiments of the comments on school redistricting in LOU Area
shape2json() | Convert the shapefile to geojson for visualization (internally convert ESPG 2236 to ESPG 4483)
MapVisualization() | Visualize the results on a interactive map.

---------------------------

### _SentiAnalysis()_
The class can take either a string or a text file as input to calculate sentiment scores. It cleans the text before the analyses. The SentiWordNet 3.0 has been used to score the sentiments of the words. Three different weighting schemes have been used. In addition, the proportion of positive, negative, and neutural feedbacks are generated as well raw scores of individual word in the data.

**Input**:
```python
'SentAnalysis().scoreText('Welcome to our new house.')'
```
**Output**:                                                                 
Mean Score (Arithmetic | Geometric | Harmonic) | Percentage (Positive | Negative | Neutral) | Raw Scores
![](result_example1.png)

---------------------------

### _shape2json()_
The class converts shapefile downloaded from Frederick County Governemnt website to geojson. Some of record names in the shapefile are not consistent, which needs to customerize before the conversion.
The ESPG of the shapefiles created by ArcGIS is 2248. Internal function _coordinateConvert()_ were created to convert the coordinates to ESPG 4326 for map plots.
The outputs are json files for each elementary, middle, and high school district.
In addition, the class provides coordinates for each school based on their address.

**Unfortunately, this two-week time window has hinder my effort to clean up the shapefiles. The polygon plots in the interactive maps are not ideal. I will come back to work on this around October.**

---------------------------

### _MapVisualization()_
This class visualize the results in a interactive map. Mulitple arguments have been listed, including coordiantes, score(mean score, percentage, or raw), option (A, B, AB) and etc.
**Input**:
```python
'MapVisualization(coordinates, score, 'A', 'Frederick, MD', 'ES.json').foliumVisual('blue')'
```
**Output**                                              
**(Please forgive me for not having time to further clean the shapefile)**
![](result_example2.png)

If you have any questions, please contact me at meng.chen03(at)gmail.com.
