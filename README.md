# Data Analysis of Crime Rates in Buffalo
## Introduction
We have performed a thorough analysis of the crime reports in Buffalo that have been reported from 2010 to the present. The dataset used for this analysis can be accessed at https://data.buffalony.gov/Public-Safety/Crime-Incidents/d6g9-xbgu. We have generated bar graphs from the analysis that depict various factors associated with the frequency of crime incidents. Moreover, we have constructed a map highlighting regions where specific crimes occur regularly. The map aims to alert the police department to prevent crimes before they happen. Ultimately, we have concluded how the analysis will aid both the police department and society at large.
## Why This Topic?
Crime is a pressing concern in society. 
Given the surging rate of criminal activity, we have conducted a thorough analysis of the available data and arrived at some vital insights. These findings will aid law enforcement agencies in identifying the regions that require heightened patrolling. Additionally, the analysis sheds light on the precautions that individuals can take to safeguard themselves.
## Data Processing
The data was imported from a CSV file into Python utilizing the CSV library. Subsequently, the data was filtered to exclude unreliable records dated before 2010, which resulted in a decrease in the total number of data points from 287,308 to 210,074. The time was transformed into a 24-hour format, and the date was isolated to form a unique column. The irrelevant columns were eliminated, and only the pertinent information, such as Case Number, Date, Time, Weekday, Incident Type, Address, Neighborhood, and Global Coordinates, was retained. Finally, the data was loaded into an SQL database for future use.

