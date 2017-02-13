import fresh_tomatoes
import media

jaan = media.Movie("jannat",
                   "http://www.impawards.com/intl/india/2008/posters/jannat_ver5.jpg",
                   "https://youtu.be/5ZsfVkp8z78")

harry =  media.Movie("Harry potter part-1", "http://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2013/09/12/101029496--sites-default-files-images-101029496-3176173-1748009911-hp.jp-1.jpg?v=1474281478", "harry potter")

mission = media.Movie("Mission Impossible", "https://i.ytimg.com/vi/ZCs3tjSZLCo/maxresdefault.jpg", "https://youtu.be/HGVjgSHUkh0")

snowden = media.Movie("snowden", "https://snowdenfilm.com/img/common/share.jpg", "Sowden")

american = media.Movie("american pie","https://www.uphe.com/sites/default/files/2015/04/American-Pie-Gallery-1.jpg", "https://youtu.be/kIIz39ZOSo4")

movies = [jaan, harry, mission, snowden, american]
fresh_tomatoes.open_movies_page(movies)
