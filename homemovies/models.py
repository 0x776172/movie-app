from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.TextField(blank=True, null=False, primary_key=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    imgpath = models.TextField(db_column='imgPath', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    duration = models.TextField(blank=True, null=True)  # This field type is a guess.
    genre = models.TextField(blank=True, null=True)  # This field type is a guess.
    language = models.TextField(blank=True, null=True)  # This field type is a guess.
    mpaarating = models.TextField(db_column='mpaaRating', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    userrating = models.TextField(db_column='userRating', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return f'''
                id: {self.id}
                name: {self.name}
                description: {self.description}
                image path: {self.imgpath}
                duration: {self.duration}
                genre: {self.genre}
                language: {self.language}
                mpaa rating: {self.mpaarating}
                user rating: {self.userrating}
                '''

