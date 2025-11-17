
library(plumber) 
library(readr)    
library(jsonlite)  


csv = "C:/Resume got self/car_sales_data.csv"  
#* @get /r
function() {
  df = read.csv(csv)           
  toJSON(df,dataframe = "rows")
}

