"""
>>> from django.contrib.auth.models import User
>>> user1 = User(username='user1')
>>> user1.save()
>>> user2 = User(username='user2')
>>> user2.save()
>>> from gallery.models import *
>>> gallery1 = Gallery(name='Gallery1')
>>> gallery1.save()
>>> gallery2 = Gallery(name='Gallery2')
>>> gallery2.save()

>>> Picture(name='Picture1',gallery=gallery1,owner=user1,image='uploads/picture1.jpg').save()
>>> Gallery.objects.get(name='Gallery1').users
u'user1'
>>> Gallery.objects.get(name='Gallery2').users
u''
>>> Gallery.objects.get(name='Gallery1').picture_count
1
>>> Gallery.objects.get(name='Gallery2').picture_count
0

>>> Picture(name='Picture2',gallery=gallery2,owner=user2,image='uploads/picture2.jpg').save()
>>> Gallery.objects.get(name='Gallery1').users
u'user1'
>>> Gallery.objects.get(name='Gallery2').users
u'user2'
>>> Gallery.objects.get(name='Gallery1').picture_count
1
>>> Gallery.objects.get(name='Gallery2').picture_count
1

>>> pic = Picture.objects.get(name='Picture2')
>>> pic.gallery = gallery1
>>> pic.save()
>>> Gallery.objects.get(name='Gallery1').users
u'user1, user2'
>>> Gallery.objects.get(name='Gallery2').users
u''
>>> Gallery.objects.get(name='Gallery1').picture_count
2
>>> Gallery.objects.get(name='Gallery2').picture_count
0

>>> Picture.objects.get(name='Picture2').delete()
>>> Gallery.objects.get(name='Gallery1').users
u'user1'
>>> Gallery.objects.get(name='Gallery2').users
u''
>>> Gallery.objects.get(name='Gallery1').picture_count
1
>>> Gallery.objects.get(name='Gallery2').picture_count
0
>>> Gallery.objects.get(name='Gallery1').picture_comment_count
0
>>> Gallery.objects.get(name='Gallery2').picture_comment_count
0

>>> user = User.objects.get(username='user1')
>>> user.username = 'somenewname'
>>> user.save()
>>> Gallery.objects.get(name='Gallery1').users
u'somenewname'

>>> pic = Picture.objects.get(name='Picture1')
>>> Comment(text='sometext',picture=pic,author=user).save()
>>> Comment.objects.get(text='sometext').title
u'Comment on Picture1 by somenewname'

>>> Gallery.objects.get(name='Gallery1').picture_comment_count
1
>>> Gallery.objects.get(name='Gallery2').picture_comment_count
0
>>> user.username = 'user1again'
>>> user.save()
>>> pic.name = 'somenewname_for_picture1'
>>> pic.save()
>>> Comment.objects.get(text='sometext').title
u'Comment on somenewname_for_picture1 by user1again'
"""
