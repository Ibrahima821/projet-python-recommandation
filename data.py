import pandas as pd

def get_movie_data():
    data = [
        {
            "id": 1,
            "title": "Harry Potter and the Sorcerer's Stone",
            "genre": "Fantasy",
            "tags": "magic wizard hogwarts fantasy adventure potter",
            "rating": "⭐⭐⭐⭐(4.6)", 
            "description": "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.",
            "image": "images/HarryPotter.jpg"
        },
        {
            "id": 2,
            "title": "The Avengers",
            "genre": "Action",
            "rating": "⭐⭐⭐⭐ (4.2)", 
            "tags": "hero action marvel superhero alien fight",
            "description": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
            "image": "images/Avengers_.jpg"
        },
        {
            "id": 3,
            "title": "Titanic",
            "genre": "Romance",
            "tags": "love romance ship drama tragedy ocean",
            "rating": "⭐⭐⭐⭐ (4)", 
            "description": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
            "image": "images/titanic.jpg"
        },
        {
            "id": 4,
            "title": "The Dark Knight",
            "genre": "Action",
            "tags": "hero batman crime dark action gotham",
            "rating": "⭐⭐⭐ (3.6)", 
            "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
            "image": "images/Thedarknight.jpg"
        },
        {
            "id": 5,
            "title": "Interstellar",
            "genre": "Sci-Fi",
            "tags": "space future science time star dimension",
            "rating": "⭐⭐⭐⭐⭐ (5)", 
            "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
            "image": "images/interstelar.jpg"
        },
        {
            "id": 6,
            "title": "The Lion King",
            "genre": "Animation",
            "tags": "animal disney king africa animation family",
            "rating": "⭐⭐⭐ (3)", 
            "description": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
            "image": "images/lionking.jpg"
        },
        {
            "id": 7,
            "title": "Inception",
            "genre": "Sci-Fi",
            "tags": "dream mind mystery action thriller puzzle",
            "rating": "⭐⭐⭐⭐(4)", 
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
            "image": "images/inception.jpg"
        },
        {
            "id": 8,
            "title": "The Notebook",
            "genre": "Romance",
            "tags": "love romance couple drama story emotional",
            "rating": "⭐⭐⭐(3)", 
            "description": "A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences.",
            "image": "images/thenotebook.jpg"
        }
    ]
    return pd.DataFrame(data)