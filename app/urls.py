from django.urls import path
from . import views
from .forms import PasswordResetConfirmForm, PasswordResetForm
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.home, name="home"),
    path('<uuid:feedback_id>/<slugified_full_name>/', views.portfolio, name="portfolio"),
    path('resume-preview/<int:pk>/', views.ViewPdf.as_view(), name='ViewPdf'), 
    path('check-pdf/<uuid:feedback_id>/', views.pdfview, name="pdfview"),
    #  path('download-pdf/<uuid:feedback_id>/', views.downloadpdf, name="downloadpdf"),
    path("create-resume/", views.create_resume, name="create_resume"),
    path("<uuid:feedback_id>/", views.Resume, name="Resume"),  
    path('download-resume/<int:pk>/', views.DownloadPdf.as_view(), name='DownloadPdf'),
    path("personal-details/<int:pk>/", views.person_details, 
    name="person_details"),
    path("resume-feedback/<uuid:feedback_id>/", views.resumeFeedback, name="resumeFeedback"),
    path("delete-resume/<uuid:feedback_id>/", views.deleteResume, name="deleteResume"),
    path("skill/<int:pk>/", views.addSkill, name="addSkill"),
    path("<uuid:feedback_id>/get-skill/<int:pk>/", views.getSkill, name="getSkill"),
    path("<uuid:feedback_id>/get-experience/<int:pk>/", views.getExperience, name="getExperience"),
    path("<uuid:feedback_id>/update-skill/<int:pk>/", views.updateSkill, name="updateSkill"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("<uuid:feedback_id>/delete-skill/<int:pk>/", views.deleteSkill, name="deleteSkill"),
    path("experience/<int:pk>/", views.addExperience, name="addExperience"),
    path("<uuid:feedback_id>/update-experience/<int:pk>/", views.updateExperience, name="updateExperience"),
    path("<uuid:feedback_id>/delete-experience/<int:pk>/", views.deleteExperience, name="deleteExperience"),
    path("project/<int:pk>/", views.addProject, name="addProject"),
    path("<uuid:feedback_id>/get-project/<int:pk>/", views.getProject, name="getProject"),
    path("<uuid:feedback_id>/update-project/<int:pk>/", views.updateProject, name="updateProject"),
    path("<uuid:feedback_id>/delete-project/<int:pk>/", views.deleteProject, name="deleteProject"),
    path("education/<int:pk>/", views.addEducation, name="addEducation"),
    path("<uuid:feedback_id>/get-education/<int:pk>/", views.getEducation, name="getEducation"),
    path("<uuid:feedback_id>/update-education/<int:pk>/", views.updateEducation, name="updateEducation"),
    path("<uuid:feedback_id>/delete-education/<int:pk>/", views.deleteEducation, name="deleteEducation"),
    path("language/<int:pk>/", views.addLanguage, name="addLanguage"),
    path("<uuid:feedback_id>/get-language/<int:pk>", views.getLanguage, name="getLanguage"),
    path("<uuid:feedback_id>/update-language/<int:pk>/", views.updateLanguage, name="updateLanguage"),
    path("<uuid:feedback_id>/delete-language/<int:pk>/", views.deleteLanguage, name="deleteLanguage"),
    path("reference/<int:pk>/", views.addReference, name="addReference"),
    path("<uuid:feedback_id>/get-reference/<int:pk>/", views.getReference, name="getReference"),
    path("<uuid:feedback_id>/update-reference/<int:pk>/", views.updateReference, name="updateReference"),
    path("<uuid:feedback_id>/delete-reference/<int:pk>/", views.deleteReference, name="deleteReference"),
    path("award/<int:pk>/", views.addAward, name="addAward"),
    path("<uuid:feedback_id>/get-award/<int:pk>/", views.getAward, name="getAward"),
    path("<uuid:feedback_id>/update-award/<int:pk>/", views.updateAward, name="updateAward"),
    path("<uuid:feedback_id>/delete-award/<int:pk>/", views.deleteAward, name="deleteAward"),
    path("organisation/<int:pk>/", views.addOrganisation, name="addOrganisation"),
    path("<uuid:feedback_id>/get-organisation/<int:pk>/", views.getOrganisation, name="getOrganisation"),
    path("<uuid:feedback_id>/update-organisation/<int:pk>/", views.updateOrganisation, name="updateOrganisation"),
    path("<uuid:feedback_id>/delete-organisation/<int:pk>/", views.deleteOrganisation, name="deleteOrganisation"),
    path("certificate/<int:pk>/", views.addCertificate, name="addCertificate"),
    path("<uuid:feedback_id>/get-certificate/<int:pk>/", views.getCertificate, name="getCertificate"),
    path("<uuid:feedback_id>/update-certificate/<int:pk>/", views.updateCertificate, name="updateCertificate"),
    path("<uuid:feedback_id>/delete-certificate/<int:pk>/", views.deleteCertificate, name="deleteCertificate"),
    path("interest/<int:pk>/", views.addInterest, name="addInterest"),
    path("<uuid:feedback_id>/get-interest/<int:pk>/", views.getInterest, name="getInterest"),
    path("<uuid:feedback_id>/update-interest/<int:pk>/", views.updateInterest, name="updateInterest"),
    path("<uuid:feedback_id>/delete-interest/<int:pk>/", views.deleteInterest, name="deleteInterest"),
    path("publication/<int:pk>/", views.addPublication, name="addPublication"),
    path("<uuid:feedback_id>/get-publication/<int:pk>/", views.getPublication, name="getPublication"),
    path("<uuid:feedback_id>/update-publication/<int:pk>/", views.updatePublication, name="updatePublication"),
    path("<uuid:feedback_id>/delete-publication/<int:pk>/", views.deletePublication, name="deletePublication"),
    path("register/", views.account_register, name="register"),
    path("login/", views.account_login, name="login"),
    path("logout/", views.account_logout, name="logout"),
    path("delete/", views.account_delete, name="delete_account"),
    path("settings/profile/", views.user_profile, name="user_profile"),
    path(
        "activate/<slug:uidb64>/<slug:token>)/",
        views.account_activate,
        name="activate_account",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/user/password-reset-form.html",
            html_email_template_name="account/user/password-reset-email.html",
            form_class=PasswordResetForm,
            success_url = 'password-reset-email-confirm/'
        ),
        name="password_reset",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/user/password-reset-confirm.html",
            form_class=PasswordResetConfirmForm,
            success_url = 'password-reset-complete/'
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/password-reset-email-confirm/",
        TemplateView.as_view(template_name="account/user/password-reset-success.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-complete/",
        TemplateView.as_view(template_name="account/user/password-reset-success.html"),
        name="password_reset_complete",
    ),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="account/user/forgot-password.html",
        ),
        name="change_password",
    ),
    path(
        "change-password-done/",
        TemplateView.as_view(template_name="account/user/password-reset-success.html"),
        name="change_password_done",
    ),
    path('cvbuild-feeback/', views.cvbuildFeedback, name='cvbuildfeedback'),
]
