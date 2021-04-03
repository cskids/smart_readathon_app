from isbnlib import meta

SERVICE = 'openl'

def get_book(isbn):
    data = meta(isbn, SERVICE)
    authors = ' '.join(data['Authors'])
    return data['Title'], authors


if __name__ == '__main__':
    print(get_book('0439412811'))
