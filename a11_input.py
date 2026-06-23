# ## 파이썬 코드 작성 프롬프트

# 상품의 이름, 가격, 할인율을 입력받아 할인 금액과 최종 가격을 계산하는 파이썬 프로그램을 작성하세요.

# 프로그램은 사용자에게 다음 정보를 입력받아야 합니다.

# 1. 상품명
# 2. 상품 가격
# 3. 할인율

# 상품 가격과 할인율은 숫자로 입력되어야 하며, 숫자가 아닌 값이 입력되면 `"가격과 할인율은 숫자로 입력해야 합니다."`라는 안내 문구를 출력해야 합니다.

# 정상적으로 숫자가 입력되면 다음 공식을 사용해 할인 금액과 최종 가격을 계산하세요.

# ```python
# 할인 금액 = 상품 가격 * 할인율 / 100
# 최종 가격 = 상품 가격 - 할인 금액
# ```

# 계산이 끝나면 상품명, 원래 가격, 할인율, 할인 금액, 최종 가격을 보기 좋게 f-string으로 출력하세요.

# 프로그램은 `main()` 함수 안에 작성하고, 파일이 직접 실행될 때만 `main()` 함수가 실행되도록 작성하세요.

# AI 활용해서 코드를 작성하세요.

def main():
    # 상품명은 한 번만 입력받습니다.
    product_name = input("상품명을 입력하세요: ")

    # 가격과 할인율을 올바르게 입력할 때까지 무한 반복합니다.
    while True:
        price_input = input("상품 가격을 입력하세요: ")
        discount_input = input("할인율(%)을 입력하세요: ")

        try:
            # 숫자로 변환을 시도합니다.
            price = float(price_input)
            discount_rate = float(discount_input)
            
            # 변환에 성공하면 break를 만나 while 문을 탈출합니다!
            break 
            
        except ValueError:
            # 숫자가 아니면 에러를 출력하고, break를 못 만나므로 다시 while문 처음으로 돌아갑니다.
            print("가격과 할인율은 숫자로 입력해야 합니다. 다시 입력해 주세요.\n")

    # [계산 및 출력 로직] 위 단계에서 올바른 값이 채워져야 이 아래로 내려옵니다.
    discount_amount = price * discount_rate / 100
    final_price = price - discount_amount

    print("\n" + "="*30)
    print(f"📦 상  품  명: {product_name}")
    print(f"💰 원래 가격: {price:,.0f}원")
    print(f"📉 할  인  율: {discount_rate:.1f}%")
    print(f"💸 할인 금액: {discount_amount:,.0f}원")
    print(f"✅ 최종 가격: {final_price:,.0f}원")
    print("="*30)

if __name__ == "__main__":
    main()
