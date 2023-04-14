"""序列化器模块"""
from rest_framework import serializers  # 导入序列化模块
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 序列化User模型
        # fields = "__all__"  # 序列化所有字段
        exclude = ('password',)  # id不参与序列化，剔除不需要序列化的字段,不能与fields同时使用
        read_only_fields = ("id",)  # id不参与反序列化
        # 定义字段校验规则
        extra_kwargs = {
            "phone": {"max_length":18,"required":False},
        }
