from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(User.objects.all(), message="username already taken.")
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(User.objects.all(), message="email already registered.")
        ],
    )
    password = serializers.CharField(write_only=True, max_length=128)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(validated_data.get("password", instance.password))
        instance.save()
        return instance

        # esse códgio de cima substitui esse de baixo
        # instance.username = validated_data.get("username", instance.username)
        # instance.email = validated_data.get("email", instance.email)
        # instance.set_password(validated_data.get("password", instance.password))
        # instance.first_name = validated_data.get("first_name", instance.first_name)
        # instance.last_name = validated_data.get("last_name", instance.last_name)
        # instance.birthdate = validated_data.get("birthdate", instance.birthdate)
        # instance.is_employee = validated_data.get("is_employee", instance.is_employee)
        # instance.save()
        # return instance

    # pode usar o validators direto no campo como está lá em cima, ou esses a baixo
    # from rest_framework.exceptions import ValidationError
    # def validate_username(self, value):
    #     if User.objects.filter(username=value).exists():
    #         raise ValidationError(f"username {value} already exists")
    #     return value

    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise ValidationError(f"email {value} already exists")
    #     return value
