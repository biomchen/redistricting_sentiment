### Sentiment Analyses of Linganore-Oakdale-Urbana Area Redistricting

Author @Meng Chen

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
![](data/survey_example.png)

The shapefiles of Frederick County School District have been downloaded at Frederick County [website](https://www.frederickcountymd.gov/5969/Download-GIS-Data). The shapefile contains the polygon data that splits the all Frederick County Public schools into different school district and were used to visualize the results. The shapefile was generated by ArcGIS under EPSG 2248. The EPSG was short for European Petroleum Survey Group but now known as the Geomatics Committee of the International Association of Oil and Gas Producers(OGP). 2248 is the EPSG spatial reference ID for Maryland. To project the Maryland to the world map, the coordinates in shapefile of Maryland were converted under the spatial reference ID EPSG 4326. See Methods for details.

---------------------------

#### Methods
___________________________

I used Python to create three classes to analyze the data and visualize the results. Each of class has specific methods to analyze data and output the results. I assemble them all together as a module named 'redistrict'. See below for details of functionality of each class as well as methods inside.

#### redistrict Module
This module includes three newly developed classes, ___SentimentAnalysis()__, ___Shape2Json()___, and ___MapVisualization()___. Each class have been developed to address certain questions during the analyses.

Class  | Description
------ | -----------
SentimentAnalysis | Build a word score dictionary based on SentiWordNet 3.0; calculate the score of the sentiment of parents' feedbacks
Shape2Json| Convert the ESRI shapefile to geojson file; convert coordinates from the Maryland geospatial reference to the world one
MapVisualization | Visualize the sentiment score of different school districts on a interactive map

---------------------------

```Python
class SentimentAnalysis():
```
In general, the class calculates the scores of the sentiments of text, and the input can be either string or text file. The results will include mean score, percentage, and row scors of all words.

```Python
def weighting(method, score_list):
```
It uses different weighting methods to calculate the mean of the sentiment score.

*Parameters* |Description
----|----
`method` | arithmetic, geometric, and harmonic
`score_list` |a list of the row sentiment scores of the words

```Python
def build_swn(base):
```
This function build a dictionary of the sentiment score of each word in the SentiWordNet 3.0. The original SentiWordNet file has been modified to remove unnecessary heading and descriptive details about the SentiWordNet project prior to input for building the dictionary.
  * Parameters:
    * base: the sentiment score data of the SentiWordNet project, version 3.0.

```Python
def clean_text(filename):
```
It changes the upper case to lower case as well removes non-word characters in a sentence or a paragraph and compile them together for scoring the sentiment.
  * Parameters:
    * filename: either an input of a string or a txt file.

```Python
def score_text():
```
This score the sentiment of words in the sentence or paragraphs, and provides the mean score (arithmetic, geometric, and harmonic) of the sentiments embeded in the words. In addition, it will calculate the percentage of positive, negative, and neural sentiment for understanding the preferences of the parents. Raw score for each word are also be recorded.
  * Parameters:
    * text: the text after cleaning.

**Input**:
```python
'SentimentAnalysis().score_text('Welcome to our new house.')'
```
**Output**:                                                                 
Mean Score (Arithmetic | Geometric | Harmonic) | Percentage (Positive | Negative | Neutral) | Raw Scores
![](results/result_example1.png)

---------------------------

```Python
class Shape2Json():
```
The class converts an ESRI shapefile into a geojson file and get the coordinates of each school. Unfortunately, during the generation of the shapefiles, both 'SCHOOL' and 'SCHOOL_1' has been used for field_attributes. the The conversion of the shapefile are two-step process using two methods.
convert_json and convert_epsg.

```Python
def convert_json():
```
It converts shapefile into geojson file.


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
![](results/result_example2.png)

If you have any questions, please contact me at meng.chen03(at)gmail.com.
