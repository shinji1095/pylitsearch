from flask import Flask, request, render_template, redirect, url_for
from pylitsearch import db, scholar

app = Flask(__name__, template_folder="/pylitsearch/templates")

# DB の初期化（初回実行時にテーブルが作成される）
db.init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_query = request.form.get("search_query")
        if search_query:
            # Google Scholar で文献を検索して取得
            papers = scholar.search_google_scholar(search_query)
            # 取得した論文を DB に追加
            for paper in papers:
                db.add_paper(paper, search_query)
            return redirect(url_for("papers"))
    return render_template("index.html")

@app.route("/papers")
def papers():
    all_papers = db.get_all_papers()
    return render_template("papers.html", papers=all_papers)

def run():
    app.run(debug=True)

if __name__ == "__main__":
    run()
