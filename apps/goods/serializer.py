from abc import ABC

from rest_framework import serializers
from .models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    """三级分类"""

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    # 在parent_category字段中定义的related_name="sub_cat"
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 商品分类
class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
