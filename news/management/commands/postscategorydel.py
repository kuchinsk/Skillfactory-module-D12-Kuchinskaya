from django.core.management.base import BaseCommand
from ...models import Post, Category

class Command(BaseCommand):
    help = 'Удаляет посты переданной категории'
    missing_args_message = 'Укажите категорию в аргументах'
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('cat', nargs='+', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["cat"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))

        try:
            category = Category.objects.get(category=options['cat'])
            Post.objects.filter(category == category).delete()
            self.stdout.write(self.style.SUCCESS('Succesfully deleted all news from category'))  # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR('Could not find category'))