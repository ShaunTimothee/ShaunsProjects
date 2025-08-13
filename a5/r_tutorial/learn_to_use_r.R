# What is R? Ris both a language and environment for statistical computing and graphics!

#Resources for clearing panes, data, memory:
# http://www.sthda.com/english/articles/17-tips-tricks/75-clear-user-interface-and-free-memory-in-rrstudio/
# http://datacornering.com/how-to-clear-rstudio-panes-with-code/

# Clear Rstudio console, environment, plot panes and free up memory at once:
rm(list = ls(envir = globalenv()), envir = globalenv()); if (!is.null(dev.list())) dev.off(); gc(); cat("\014")

# Breakdown
# 1. Clear Rstudio console window (identical to Ctrl+L):
# cat("\014")
#
# 2. Clear Rstudio environment window (equivalent to click button clear objects from workspace in enviorment panel)
# rm(list=ls(envir = globalenv()), envir = globalenv())
#
# 3. Clear Rstudio plot window (equivalent to click on button clear all plots in in plots panel)
# if(!is.null(dev.list())) dev.off()

# 4. Free up memory for Rstudio:
#gc()

#set working directory
# setwd("C:\Users\shaun\OneDrive\Documents\repos\lis4369\a5\r_tutorial")
setwd('C:/Users/shaun/OneDrive/Documents/repos/lis4369/a5/r_tutorial')

# pdf(file="C:\Users\shaun\OneDrive\Documents\repos\lis4369\a5\r_tutorial/myplotfile.pdf")

install.packages("quantmod", dependencies = TRUE)
install.packages("dplyr", dependencies = TRUE)
install.packages("ggplot2", dependencies = TRUE)



library("quantmod")
getSymbols("AAPL")

barChart(AAPL)
barChart(AAPL, subset='last 14 days')
chartSeries(AAPL, subset='last 14 days')
barChart(AAPL['2013-04-1::2013-04-12'])
barChart(AAPL['2013-04-1::'])
barChart(AAPL['2020'])


