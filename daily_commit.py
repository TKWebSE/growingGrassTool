import os
import datetime
import random
import subprocess # subprocessモジュールをインポート

def create_and_commit():
    # ユーザー名とメールアドレスを取得
    git_username = os.environ.get('GIT_USERNAME')
    git_useremail = os.environ.get('GIT_USEREMAIL')

    if not git_username or not git_useremail:
        print("Error: GIT_USERNAME and GIT_USEREMAIL environment variables must be set.")
        return

    # タイムスタンプを使ってユニークなファイル名を作成
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"daily_update_{timestamp}.txt"
    
    # コミットメッセージ
    commit_message = f"Daily automated commit: {timestamp}"

    try:
        # 既存のファイルに追記するか、新しいファイルを作成
        with open("daily_log.txt", "a") as f:
            f.write(f"Commit on {timestamp}: {random.randint(1, 100)}\n")
        
        # Gitコマンドの実行
        # subprocess.run() を使用して、より安全にコマンドを実行
        subprocess.run(["git", "config", "user.name", git_username], check=True)
        subprocess.run(["git", "config", "user.email", git_useremail], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True) # もしデフォルトブランチがmasterならmasterにしてください

        print(f"Successfully committed: {commit_message}")

    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print(f"Error output: {e.stderr.decode()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_and_commit()
