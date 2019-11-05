from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from .forms import SignupForm
from django.conf import settings
from django.contrib import messages
# Create your views here.
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

'''
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 가입과 동시에 여기에서 로그인 처리하기
            auth_login(request, user)  # form_valid 함수에 들어 있음
            next_url = request.GET.get('next') or 'profile' # 회원가입시에 next 인자 처리하기 위해 request의 GET querydict에서 next인자를 가져옴. 없으면 profile로 이동
            #return redirect('settings.LOGIN_URL')  # 가입 성공하면 로그인 페이지로 이동
            return redirect('next_url')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form,})
'''

class SignupView(CreateView):
    model = User,
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        #return '/admin/'  # admin으로 직접 갈 경우에는 이렇게 설정
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

'''signup = CreateView.as_view(model=User,
                            form_class=UserCreationForm,
                            success_url=settings.LOGIN_URL,
                            template_name="accounts/signup.html")'''


class MyPasswordChangeView(PasswordChangeView):
    template_name='accounts/password_change_form.html'
    success_url=reverse_lazy('profile')

    def form_valid(self, form):
        messages.info(self.request, '비밀번호 변경을 완료했습니다.')
        return super().form_valid(form)

password_change = MyPasswordChangeView.as_view()
