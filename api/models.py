from django.db import models

class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    AuthorName = models.CharField(max_length=50)

    def __str__(self):
        return self.AuthorName

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.Title

class Member(models.Model):
    MemberID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    ContactInfo = models.IntegerField()
    Email = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class BorrowRecord(models.Model):
    BorrowID = models.AutoField(primary_key=True)
    Borrow_Date = models.DateField()
    Return_Date = models.DateField(null=True, blank=True)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='records')
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='records')

    def __str__(self):
        return f"Borrow {self.BorrowID} - {self.Book.Title} by {self.Member.Name}"
