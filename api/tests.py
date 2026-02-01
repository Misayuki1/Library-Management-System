from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book, Member, BorrowRecord
from datetime import date

class LibraryCRUDTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(AuthorName="J.K. Rowling")
        self.book = Book.objects.create(Title="Harry Potter", Author=self.author)
        self.member = Member.objects.create(Name="John Doe", ContactInfo=123456789, Email="john@example.com")
        self.borrow_record = BorrowRecord.objects.create(
            Borrow_Date=date.today(),
            Book=self.book,
            Member=self.member
        )

    # create 
    def test_create_author(self):
        url = reverse('author-list')
        data = {'AuthorName': 'George R.R. Martin'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    def test_create_book(self):
        url = reverse('book-list')
        data = {'Title': 'A Game of Thrones', 'Author': self.author.AuthorID}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # read 
    def test_get_authors(self):
        url = reverse('author-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_author_detail(self):
        url = reverse('author-detail', args=[self.author.AuthorID])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['AuthorName'], "J.K. Rowling")

    # update
    def test_update_author(self):
        url = reverse('author-detail', args=[self.author.AuthorID])
        data = {'AuthorName': 'Joanne Rowling'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.AuthorName, 'Joanne Rowling')

    # delete
    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.BookID])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # borrow records
    def test_create_borrow_record(self):
        url = reverse('borrowrecord-list')
        data = {
            'Borrow_Date': str(date.today()),
            'Book': self.book.BookID,
            'Member': self.member.MemberID
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
