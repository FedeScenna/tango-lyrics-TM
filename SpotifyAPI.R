library(Rspotify)

#Get songs from "Tangos y Milongas" playlist
songs <- getPlaylistSongs("spotify","37i9dQZF1DXcCT9tm6fRIV",token=keys)

#Get the features of each song in a new dataframe.
features<-data.frame()
for (i in 1:nrow(songs)){
  ft<-getFeatures(songs$id[i], token=keys)
  features <- rbind(features, ft)
}

#Merge two dataframes in one
songs <- merge(songs, features, by="id")
