from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

_DEFAULT_EMAIL_DOMAIN = "example.com"
User = get_user_model()


class Command(BaseCommand):
    help = "Create an unprivileged user"

    def add_arguments(self, parser):
        credentials = parser.add_argument_group("credentials")
        credentials.add_argument(
            "--user", metavar="USER", dest="username", help="user name"
        )
        credentials.add_argument("--password", metavar="PASSWORD", help="password")
        credentials.add_argument("--email", metavar="EMAIL", help="e-mail address")

    def _report_success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def _require_identical_configuration(self, user, password, email):
        if not user.check_password(password):
            raise CommandError(
                'User "{}" exists but password differs.'.format(user.username)
            )

        if user.email != email:
            raise CommandError(
                'User "{}" exists but e-mail address differs.'.format(user.username)
            )

    def _create_new_user(self, username, password, email):
        return User.objects.create_user(
            username=username, password=password, email=email
        )

    def handle(self, *args, **options):
        username = options["username"]
        password = options["password"]
        email = options["email"]

        if email is None:
            email = "{}@{}".format(username, _DEFAULT_EMAIL_DOMAIN)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = self._create_new_user(username, password, email)
                user.save()
            except Exception as e:
                raise CommandError("Could not create user: {}".format(e))

            self._report_success(
                'Superuser "{}" with e-mail address "{}"'
                " created.".format(username, email)
            )
        else:
            self._require_identical_configuration(user, password, email)
            self._report_success(
                'User "{}" with identical configuration '
                "exists, nothing more to do.".format(username)
            )
