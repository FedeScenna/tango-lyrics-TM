
library(tm)
library(tidyverse)
data <- read.csv("tango_lyrics.csv", sep=";")
lyrics<-Corpus(VectorSource(data$lyric))
lyrics <- tm_map(lyrics, removeNumbers)
lyrics <- tm_map(lyrics, removePunctuation)
lyrics_dtm <- DocumentTermMatrix(lyrics)
freq<- colSums(as.matrix(lyrics_dtm))
