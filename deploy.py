import subprocess
import shutil
import os
import sys
from datetime import datetime

def run(cmd, check=True):
    print(f"\n>>> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if check and result.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        sys.exit(result.returncode)

def ensure_git_repo():
    try:
        subprocess.check_output("git rev-parse --is-inside-work-tree", shell=True)
    except subprocess.CalledProcessError:
        print("❌ This directory is NOT a git repository.")
        print("👉 Run: git init && git remote add origin <repo-url>")
        sys.exit(1)

def auto_commit_if_needed():
    status = subprocess.check_output(
        "git status --porcelain", shell=True
    ).decode().strip()

    if not status:
        print("✅ Git working tree clean.")
        return

    print("⚠️ Uncommitted changes detected.")
    print("📦 Auto-committing changes before deploy...")

    # Make sure _site is never committed on main
    with open(".gitignore", "a+", encoding="utf-8") as f:
        f.seek(0)
        if "_site/" not in f.read():
            f.write("\n_site/\n")

    run("git add .gitignore")
    run("git add .")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run(f'git commit -m "Auto commit before deploy ({timestamp})"')
    run("git push")

def build_site():
    print("\n🔨 Building Jekyll site locally...")
    run("bundle install")
    run("bundle exec jekyll build")

def run_scholar():
    scholar_script = "_scripts/scholar_update.py"
    if os.path.isfile(scholar_script):
        print("\n📚 Running Google Scholar update...")
        run(f"python {scholar_script}")
        auto_commit_if_needed()
    else:
        print("ℹ️ Scholar script not found, skipping.")

def deploy_to_gh_pages():
    if not os.path.isdir("_site"):
        print("❌ _site directory not found. Build failed.")
        sys.exit(1)

    print("\n🚚 Deploying _site to gh-pages...")

    # Remember current branch
    current_branch = subprocess.check_output(
        "git branch --show-current", shell=True
    ).decode().strip()

    # Check if gh-pages already exists
    branches = subprocess.check_output(
        "git branch --list gh-pages", shell=True
    ).decode().strip()

    if branches:
        print("🔄 gh-pages branch exists, resetting it")
        run("git checkout gh-pages")
    else:
        print("🆕 Creating gh-pages orphan branch")
        run("git checkout --orphan gh-pages")
    # Copy site output
    for item in os.listdir("_site"):
        src = os.path.join("_site", item)
        dst = item

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

    # Disable GitHub Jekyll
    open(".nojekyll", "w").close()

    run("git add .")
    run('git commit -m "Deploy static site"')
    run("git push origin gh-pages --force")

    # Return to original branch
    run(f"git checkout {current_branch}")


def main():
    print("🚀 Deploying Jekyll site (local full build → GitHub Pages)")
    ensure_git_repo()
    auto_commit_if_needed()
    run_scholar()
    build_site()
    deploy_to_gh_pages()
    print("\n✅ Deployment complete!")

if __name__ == "__main__":
    main()
