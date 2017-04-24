library(Rspotify)
keys <- spotifyOAuth("Tango SA","8040524868f74349ae250722a251bb59","623bcbdbedaa48ff9ad0eb40fdf7db7a")
songs <- getPlaylistSongs("spotify","37i9dQZF1DXcCT9tm6fRIV",token=keys)

spotify_df<-data.frame()

for (i in 1:nrow(songs)){
  
  temp_df<-as.data.frame(songs$tracks[i])
  temp_df<-cbind(temp_df, songs$artist[i])
  temp_df<-cbind(temp_df,getFeatures(songs$id[i], token=keys))
  spotify_df<-rbind(spotify_df, temp_df)
}

library(data.table)
setnames(spotify_df, old = c('songs$tracks[i]','songs$artist[i]'), new = c('Song','Artist'))
