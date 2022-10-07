# Generated by Django 4.1.1 on 2022-10-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_award_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="personal_details",
            name="angellist",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="appstore",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="artstation",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="behance",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="bitbucket",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="bitcoin",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="blogger",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="codechef",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="codeforces",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="codepen",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="codewars",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="coursera",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="dev_to",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="deviantart",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="discord",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="dribble",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="facebook",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="fiverr",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="flickr",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="geeksforgeeks",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="gitea",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="github",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="gitlab",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="googleplay",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="googlescholar",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="hackerearth",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="hackerrank",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="hackthebox",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="hashnode",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="imdb",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="instagram",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="kaggle",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="leetcode",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="line",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="linkedin",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="medium",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="orcid",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="paypal",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="pininterest",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="pluralsight",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="producthunt",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="protonmail",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="qq",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="quora",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="qwiklabs",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="reddit",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="researchgate",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="reverbnation",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="sanpchat",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="signal",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="skype",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="slack",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="spotify",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="stackoverflow",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="telegram",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="tiktok",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="tripadvisor",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="tryhackme",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="tumbir",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="twitter",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="upwork",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="vimeo",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="vsco",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="website",
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="wechat",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="whatsapp",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="wordpress",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="xing",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="yelp",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="personal_details",
            name="youtube",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name="Links",
        ),
    ]
