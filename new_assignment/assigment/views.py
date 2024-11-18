from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MessageForm
# Create your views here.


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Here, you can integrate your email sending logic, for example:
            # send_mail(form.cleaned_data['email_title'], form.cleaned_data['message_body'], form.cleaned_data['sender_email'], [form.cleaned_data['receiver_email']])

            messages.success(request, 'Message sent successfully!')
            return redirect('blog/post.html')  # Or wherever you want to redirect after success
        else:
            messages.error(request, 'Error: ' + str(form.errors))
            return render(request, 'blog/post.html', {'form': form})
    else:
        form = MessageForm()

    return render(request, 'blog/post.html', {'form': form})




