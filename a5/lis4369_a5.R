# Resources for clearing panes, data, memory:
# http://www.sthda.com/english/articles/17-tips-tricks/75-clear-user-interface-and-free-memory-in-rrstudio/
# http://datacornering.com/how-to-clear-rstudio-panes-with-code/

# Clear Rstudio console, enviorment, plot panes and free up memory space at once.
rm(list =ls(envir = globalenv()), envir = globalenv()); if(!is.null(dev.list())) dev.off; gc(); cat("\014")

# Breakdown:
# 1. Clear Rstudio console window (identical to Crtl L):
# cat("\014")
#
# 2. Clear Rstudio enviorment window (equivalent to click button clear objects from workspace in enviormet panel)
# rm(list= ls(envir = globalenv()), envir+ global env())
#
# 3. Clear Rstudio plot window (equivalent to click on button clear all plots in plots panel)
# if(!is.null(dev.list())) dev.off
#
# 4. Free up memory for Rstudio:
# gc()

# set working directory (*MY* working directory--YOURS wil be different):
setwd("C:/Users/shaun/OneDrive/Documents/repos/lis4369/a5")


# https://ww.cyclismo.org/tutorial/R/
# https://www.r-tutor.com/r-intorduction

a <- 9

a + 5 # print a + 5

b <- sqrt(a) # assign square root of a to b
b

# Nonscalar data types:
# Easiest way to store list of numbers, through assignment , using c command.
# Note: c means "combine"
# vectors (one dimesional arrays), by default, are specified with the c command.
c <- -c(1,2,3,5.3,6,-2,4)

print(c)

typeof(c)

is.list(c)
is.vector(c)

d <- c("one", "two", "three")
d

typeof(d)

e <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE)
e

typeof(e)




d[1]

my_str <- "Hello World!"
my_str

typeof(my_str)

sqrt(a)

sqrt(c)

a^2

c^2

min(c)

max(c)

mean(c)

sum(c)





url = "https://raw.github.com/vincentarelbundock/Rdatasets/master/csv/Stat2Data/Titanic.csv"
titanic <- read.csv(file=url,head=TRUE,sep=",")

titanic

summary(titanic)


dir()

getwd()

names(titanic)



titanic$Name

titanic$Age

attributes(titanic)

ls()


mean(titanic$Age)

mean(titanic$Age, na.rm=TRUE)
median(titanic$Age, na.rm=TRUE)
quantile(titanic$Age, na.rm=TRUE)
min(titanic$Age, na.rm=TRUE)
max(titanic$Age, na.rm=TRUE)
var(titanic$Age, na.rm=TRUE)
sd(titanic$Age, na.rm=TRUE)

summary(titanic$Age, na.rm=TRUE)

titanic[!complete.cases(titanic),]


titanic_no_missing_data <- na.omit(titanic)
titanic_no_missing_data 


help(stripchart)
stripchart(titanic_no_missing_data$Age)

hist(titanic_no_missing_data$Age,main="Distribution of Tianic Passengers Ages",xlab="Ages")


boxplot(titanic_no_missing_data$Age)


boxplot(titanic_no_missing_data$Age,
        main='Distribution of Tianic Passengers Ages',
        xlab='Ages', 
        horizontal=TRUE)


plot(titanic_no_missing_data$Age, titanic_no_missing_data$Survived,
     main="Relationship Between Ages and Survival",
     xlab="Age",
     ylab="Survived")


