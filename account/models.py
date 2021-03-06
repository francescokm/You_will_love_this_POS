from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 



class Account_Manager(BaseUserManager):

    def create_user(self,email,username,first_name,last_name,phone,password=None):
        if not first_name:
            raise ValueError("You should Enter First Name to be user")
        if not last_name:
            raise ValueError("You should Enter Last Name to be user")
        if not email:
            raise ValueError("You should Enter Email to be user")
        if not username:
            raise ValueError("You should Enter Username ")
        if not phone:
            raise ValueError("You should Enter phone ")
        user = self.model(
            first_name      =   first_name,
            last_name       =   last_name,
            email           =   self.normalize_email(email),
            username        =   username,
            phone           =   phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return  user


    def create_superuser(self,email,username,phone,first_name,last_name,password=None):
        user                =   self.create_user(
            first_name      =   first_name,
            last_name       =   last_name,

            email           =   self.normalize_email(email),
            phone           =   phone,
            password        =   password,
            username        =   username,
        )
        
        user.is_admin       =   True
        user.is_staff       =   True
        user.is_superuser   =   True


        user.save(using=self._db)
        return  user






class Account(AbstractBaseUser):
    
    first_name              =   models.CharField(max_length=40,null=True)
    last_name               =   models.CharField(max_length=40,null=True)
    email                   =   models.EmailField(unique=True)
    username                =   models.CharField(unique=True,max_length=20)
    phone                   =   models.CharField(unique=True,max_length=40,null=True)
    date_joined             =   models.DateTimeField(auto_now_add=True)
    last_login              =   models.CharField(max_length=255,null=True,blank=True)
    is_admin                =   models.BooleanField(default=False,null=True)
    is_active               =   models.BooleanField(null=True,default=True)
    is_staff                =   models.BooleanField(null=True)
    is_superuser            =   models.BooleanField(null=True)
    

    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   ['username','phone','first_name','last_name']

    def __str__(self):
        return  self.email
    objects         =   Account_Manager()
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True