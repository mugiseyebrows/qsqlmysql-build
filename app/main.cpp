#include <QApplication>

#include <QListView>
#include <QStringListModel>
#include <QSqlDatabase>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QListView view;
    auto* model = new QStringListModel(QSqlDatabase::drivers());
    view.setModel(model);
    view.show();

    return a.exec();
}
