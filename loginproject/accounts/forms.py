from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    # 방법 1) 이메일로 회원가입하기
    '''def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)  # 이 자체가 이메일 유효성 검증
        return value'''

    # 방법 2)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = [validate_email]
        self.fields['username'].help_text = 'Enter Email Format'
        self.fields['username'].label = 'Email'

    # 이메일 정보를 동시에 프로파일에 저장하기
    def save(self, commit=True):
        user = super().save(commit=False) # user객체 만들고
        user.email = user.username  # user의 이메일 정보란에 username으로 획득한 이메일 정보를 저장
        if commit:
            user.save()
        return user
