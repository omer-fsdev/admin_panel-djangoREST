from product.models import *
from faker import Faker

"""
    $ pip install faker
    $ pip freeze > requirements.txt
    $ python manage.py shell
    >>> from product.faker import runProduct
    >>> runProduct()
    >>> exit() 
"""


# Product:
def runProduct():
    faker = Faker()  # Faker(['tr-TR'])

    for _ in range(200):
        product = Product(
            name=faker.domain_word(),
            description=faker.paragraph(),
            is_in_stock=faker.pybool(),
        )
        product.save()

    print("Finished")


# Review:
def runReview():
    faker = Faker()

    for product in Product.objects.iterator():
        reviews = [Review(review=faker.paragraph(), product=product) for _ in range(3)]
        Review.objects.bulk_create(reviews)

    print("Finished")


# """
#    migrations unutma
#     $ python manage.py shell
#     >>> from product.faker import runReview
#     >>> runReview()
#     >>> exit() 
# """
