from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from customer.models import Category, Customer
from customer.models import Product
from customer.forms import CustomerForm


# Create your views here.

def welcome(request):
    list_des_profs = [
        {
            'name': "alasane",
            'topic': "Droit"
        },
        {
            'name': "fall",
            'topic': "stats"
        },
        {
            'name': "diop",
            'topic': "finance"
        }
    ]

    customers = Customer.objects.all()

    context = {
        "list_profs": list_des_profs,
        "list_customers": customers
    }

    return render(request, "customer/welcome.html", context)


def all_customers(request):
    customer_list = Customer.objects.all()

    context = {
        "customers": customer_list
    }

    return render(request, "customer/customers.html", context)


def all_products(request):
    product_list = Product.objects.all()
    context = {
        "products": product_list
    }

    return render(request, "customer/products.html", context)


def all_categories(request):
    category_list = Category.objects.all()
    context = {
        "categories": category_list
    }

    return render(request, "customer/category.html", context)


def detail_category(request, id):
    category = Category.objects.get(pk=id)

    context = {
        "category": category
    }

    return render(request, "customer/detail_category.html", context)


def one_customer(request):
    return HttpResponse("Detail sur un client")


def create_customer(request):
    if request.method == "POST" and request.FILES:

        # 1- je dois créer un formulaire à partir des infos qui arrivent
        customer_form = CustomerForm(request.POST, request.FILES)
        # 2- je dois vérifier que ces infos sont valides
        if customer_form.is_valid():
            # 3- si ils sont valid, alors je les enregistre dans la base de donnée
            customer_form.save()
            # 4- et je retourne vers la liste des clients pour les afficher
            return redirect("customers")
        # 5- sinon je lui affiche le formulaire pour qu'il corrige
        else:
            context = {
                "customer_form": customer_form
            }

            return render(request, "customer/create_customer.html", context)
    else:

        customer_form = CustomerForm()

        context = {
            "customer_form": customer_form
        }

        return render(request, "customer/create_customer.html", context)


def show_customer(request, id):
    customer = Customer.objects.get(pk=id)

    context = {
        "client": customer
    }

    return render(request, "customer/show_customer.html", context)


def update_customer(request, id):
    customer_to_edit = get_object_or_404(Customer, pk=id)
    # customer_to_edit = Customer.objects.get(pk=id)

    if request.method == "POST" and request.FILES:
        # 1- je crée un formulaire avec les anciennes infos du client récupéré dans la BDD, et les nouvelles infos qui viennent du navigateur
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer_to_edit)
        # 2- je verifie si c'est valide
        if customer_form.is_valid():
            # 3- si c'est valide j'enregistre dans la base de données
            customer_form.save()
            # 4- ensuite je rediriger vers la liste des customers
            return redirect("customers")
        # 5- sinon je lui retourne le formulaire avec les infos du client non modifiées
        else:
            customer_form = CustomerForm(instance=customer_to_edit)

            context = {
                "form": customer_form
            }

            return render(request, "customer/update_customer.html", context)


    else:

        customer_form = CustomerForm(instance=customer_to_edit)

        context = {
            "form": customer_form,
            "customer": customer_to_edit
        }

        return render(request, "customer/update_customer.html", context)


def delete_customer(request, id):
    # 1- je chercher dans la base de données si il existe un customer avec cet ID
    # customer_to_delete = Customer.objects.get(pk=id)

    customer_to_delete = get_object_or_404(Customer, pk=id)
    # 2- si oui je supprime ce customer
    customer_to_delete.delete()
    # 3- je redirige vers la liste des customers
    return redirect("customers")