from django.db import models
from django.core.exceptions import ValidationError


class Image(models.Model):
    image = models.ImageField(upload_to="image")
    def __str__(self):
        return self.image.name


class Fakultet(models.Model):
    fakultet = models.CharField(max_length=100, null=True, blank=True, verbose_name='Fakultet')

    class Meta:
        verbose_name_plural = "Fakultetlar"

    def __str__(self):
        return self.fakultet


class Fanlar(models.Model):
    fan = models.CharField(max_length=50, null=True, verbose_name='Fan nomi')

    class Meta:
        verbose_name_plural = "Fanlar"

    def __str__(self):
        return self.fan

class Yonalishlar(models.Model):
    yonalish = models.CharField(max_length=100, verbose_name="yo'nalish")

    class Meta:
        verbose_name_plural = "Yonalishlar"

    def __str__(self):
        return self.yonalish

class Oqituvchilar(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Ism')
    last_name = models.CharField(max_length=30, verbose_name='Familiya')
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE, verbose_name='Fakultet')

    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name_plural = "Oqituvchilar"

class Talaba(models.Model):
    KURS = [
        ("1", "birinchi kurs"),
        ("2", "ikkinchi kurs"),
        ("3", "uchinchi kurs"),
        ("4", "to'rtinchi kurs")
    ]
    DARAJA = [
        ('bakalavr', 'Bakalavr'),
        ('magistr', 'Magistr')
    ]
    first_name = models.CharField(max_length=30, verbose_name='Ism')
    last_name = models.CharField(max_length=30, verbose_name='Familiya')
    manzil = models.CharField(max_length=150, verbose_name='Manzil')
    image = models.ManyToManyField(to=Image, null=True)
    daraja = models.CharField(max_length=10, default=True, choices=DARAJA)
    kurs = models.CharField(max_length=2, choices=KURS, verbose_name='Kurs')
    guruh_n = models.CharField(max_length=15, verbose_name='Guruh nomeri')
    pasp_s = models.CharField(max_length=2, verbose_name='Pasport seriyasi')
    pasp_n = models.CharField(max_length=7, verbose_name='Pasport raqami')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Qayta tahrirlangan vaqti')
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE, verbose_name='Fakultet')

    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name_plural = "Talabalar"

class Baholar(models.Model):
    def validate_semestr(value):
        if value < 12:
            return value
        else:
            raise ValidationError("Siz 12 dan katta son kiritolmaysiz!")
    def validate_ball(value):
        if value < 5:
            return value
        else:
            raise ValidationError("Siz 5 dan katta baxo qo'yolmaysiz!")
    semestr = models.SmallIntegerField(validators=[validate_semestr], verbose_name='Semestr', default=1)
    ball = models.SmallIntegerField(validators=[validate_ball],  verbose_name='Baho', default=2)
    sana_kir = models.DateTimeField(auto_now_add=True)
    sana_updated = models.DateTimeField(auto_now=True)
    oqituvchi = models.ForeignKey(Oqituvchilar, on_delete=models.CASCADE, verbose_name="O'qituvchi")
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE, verbose_name='Talaba')
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE, verbose_name='Fakultet')
    yonalish = models.ForeignKey(Yonalishlar, on_delete=models.CASCADE, verbose_name="Yo'nalish")
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE, verbose_name='Fan nomi')

    class Meta:
        verbose_name_plural = "Baholar"







