# Generated by Django 3.2.20 on 2023-09-07 19:11

from django.db import migrations

from sentry.new_migrations.migrations import CheckedMigration


class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production. For
    # the most part, this should only be used for operations where it's safe to run the migration
    # after your code has deployed. So this should not be used for most operations that alter the
    # schema of a table.
    # Here are some things that make sense to mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that they can
    #   be monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   have ops run this and not block the deploy. Note that while adding an index is a schema
    #   change, it's completely safe to run the operation after the code has deployed.
    is_dangerous = False

    dependencies = [
        ("sentry", "0544_add_commitfilechange_language_col"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="groupsubscription",
                    name="team",
                ),
                migrations.RemoveConstraint(
                    model_name="groupsubscription",
                    name="subscription_team_or_user_check",
                ),
                migrations.AlterUniqueTogether(
                    name="groupsubscription",
                    unique_together={
                        ("group", "user_id"),
                    },
                ),
            ],
            database_operations=[
                migrations.RunSQL(
                    reverse_sql="""
                    ALTER TABLE sentry_groupsubscription ADD COLUMN team_id BIGINT NULL;
                    ALTER TABLE sentry_groupsubscription ADD CONSTRAINT "subscription_team_or_user_check" CHECK (team_id IS NOT NULL AND user_id IS NULL OR team_id IS NULL AND user_id IS NOT NULL);
                    """,
                    sql="""
                    ALTER TABLE sentry_groupsubscription DROP CONSTRAINT IF EXISTS subscription_team_or_user_check;
                    ALTER TABLE sentry_groupsubscription DROP COLUMN IF EXISTS team_id;
                    """,
                    hints={"tables": ["sentry_groupsubscription"]},
                )
            ],
        )
    ]
