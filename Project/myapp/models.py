from django.db import models

# Create your models here.

class ProductMaster(models.Model):
	product_id=models.AutoField(primary_key=True)
	product_name=models.CharField(max_length=250,unique=True)

	def __str__(self):
		return f"{self.product_id}: {self.product_name}"

class ProductSubCategory(models.Model):
	product=models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
	product_price=models.IntegerField(max_length=10)
	product_image=models.ImageField(upload_to="product_images/")
	product_model=models.CharField(max_length=50)
	product_ram=models.CharField(max_length=20)

	def __str__(self):
		return f"{self.product.product_name} -Model: {self.product_model}, Ram: {self.product_ram}"