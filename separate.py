import pandas as pd

df = pd.read_csv (r'Human.csv')

#Find the annotations that contain Orca & listener_count that is more than 10 people
orcaDf = df.loc[(df.description.str.contains("orca", na=False)) & (df['listener_count']>10)]
print(orcaDf)


print(orcaDf[['playlist_timestamp','player_offset','feed_id','listener_count','description']])
#Use the OrcaDef to do cluster

#feed  35-> rpi_port_townsend
#feed   2-> rpi_bush_point
#feed   1-> rpi_orcasound_lab