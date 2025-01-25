import random
import sys

def write_to_terminal(text):
    """ターミナルに直接書き込む"""
    sys.stdout.buffer.write(text.encode('utf-8'))
    sys.stdout.buffer.write(b'\n')
    sys.stdout.buffer.flush()

def main():
    # ランダムな数を生成
    number = random.randint(1, 1000)
    
    # メッセージを出力
    write_to_terminal("1から1000までのランダムな数を生成します")
    write_to_terminal(f"生成された数値: {number}")

if __name__ == "__main__":
    main()