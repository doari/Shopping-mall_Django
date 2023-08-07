from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

# ListView : ListView를 사용하면 데이터베이스에서 목록을 가져와서 
# 템플릿에 어떤 데이터 타입이든 쉽게 전달하는 작업을 수행해줌 
class ProductList(ListView):
    model=Product
    context_object_name='product_list'
    template_name='product.html'
    #paginate_by=10 # 한페이지에 최대 10개의 상품 표시

class ProductCreate(FormView):
    template_name='register_product.html'
    form_class=RegisterForm
    success_url='/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'), 
            price=form.data.get('price'), 
            description=form.data.get('description'), 
            stock=form.data.get('stock') 
            )
        product.save()

        return super().form_valid(form)
    
class ProductDetail(DetailView):
    queryset = Product.objects.all()
    context_object_name='product'
    template_name='product_detail.html'

    # **kwargs : 함수에 정해지지 않은 매개변수의 가변갯수을 활요하여 오버라이딩함
    # 상세정보의 필드를 가변적으로 선택하여 보여줄수 있음
    def get_context_data(self, **kwargs):
        # 기본적인 Product의 데이터 가져오기
        context=super().get_context_data(**kwargs)
        # Order의 OrderForm에서 받아온 데이터 추가
        context['form']=OrderForm(self.request)
        return context





