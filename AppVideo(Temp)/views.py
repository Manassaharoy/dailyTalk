# from django.shortcuts import render, HttpResponseRedirect
# from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
# # from AppVideo.models import streamVideo, comments, likes
# from django.urls import reverse, reverse_lazy
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# # from AppVideo.forms import CommentForm
# import uuid


# # Create your views here.

# # def videolist(request):
# #     return render(request, 'AppVideo/videolist.html', context={})


# class MyVideos(LoginRequiredMixin, TemplateView):
#     template_name = 'AppVideo/myvideos.html'

# class UploadVideo(LoginRequiredMixin, CreateView):
#     model = streamVideo
#     template_name = 'AppVideo/uploadvideo.html'
#     fields = ('title', 'videoURL',)

#     def form_valid(self, form):
#         video_obj = form.save(commit=False)
#         video_obj.uploader = self.request.user
#         title = video_obj.title
#         video_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
#         video_obj.save()
#         return HttpResponseRedirect(reverse('homepage'))

# class VideoList(ListView):
#     context_object_name = 'videos'
#     model = streamVideo
#     template_name = 'AppVideo/videolist.html'

# # @login_required
# # def VideoDetails(request, slug):
#     # video = streamVideo.objects.get(slug=slug)
# #     comment_form = CommentForm()
# #     already_liked = likes.objects.filter(video=video, user= request.user)
# #     if already_liked:
# #         liked = True
# #     else:
# #         liked = False
# #     if request.method == 'POST':
# #         comment_form = CommentForm(request.POST)
# #         if comment_form.is_valid():
# #             comment = comment_form.save(commit=False)
# #             comment.user = request.user
# #             comment.video = video
# #             comment.save()
# #             return HttpResponseRedirect(reverse('AppVideo:videodetails', kwargs={'slug':slug}))
# # return render(request, 'AppVideo/videodetails.html', context={'video':video, 'comment_form':comment_form, 'liked':liked, })

# # @login_required
# # def liked(request, pk):
# #     video = streamVideo.objects.get(pk=pk)
# #     user = request.user
# #     already_liked = likes.objects.filter(video=video, user=user)
# #     if not already_liked:
# #         liked_post = likes(video=video, user=user)
# #         liked_post.save()
# #     return HttpResponseRedirect(reverse('AppVideo:videodetails', kwargs={'slug':video.slug}))

# # @login_required
# # def unliked(request, pk):
# #     video = streamVideo.objects.get(pk=pk)
# #     user = request.user
# #     already_liked = likes.objects.filter(video=video, user=user)
# #     already_liked.delete()
# #     return HttpResponseRedirect(reverse('AppVideo:videodetails', kwargs={'slug':video.slug}))

# # class UpdateVideo(LoginRequiredMixin, UpdateView):
# #     model = streamVideo
# #     fields = ('title', 'videoURL',)
# #     template_name = 'AppVideo/editvideo.html'

# #     def get_success_url(self, **kwargs):
# #         return reverse_lazy('AppVideo:videodetails', kwargs={'slug':self.object.slug})
