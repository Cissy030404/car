import streamlit as st

st.title('汽车租赁系统')

st.write('我们将获取您的定位权限，您是否同意?')

if st.checkbox('我同意'):

    st.header('1.租车信息填写')

    options = st.multiselect(
        '您想租什么类型的车？',
        ['跑车', '五座车', '商务车' ])	

    st.write('您选择了:', options)

    option = st.selectbox(
    '您希望您所租的车是否在保?',
    ('是', '否'))

    st.write('您选择了:', option)

    import datetime
    import streamlit as st

    d = st.date_input(
        "您将在哪天租用车辆？",
        datetime.date(2023, 3, 8))
    st.write('您租车的起始时间是:', d)

    st.header('2.客户信息填写')
    name = st.text_input('请填写您的姓名', '姓名')
    sex = st.selectbox('性别',('男', '女'))

    title = st.text_input('请输入您的身份证号码')
    st.write('您的身份证号码是', title)

    title = st.text_input('请输入您的驾驶证号码')
    st.write('您的驾驶证号码是', title)
    uploaded_files = st.file_uploader("请上传您的驾驶证照片", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)  

    if st.button('提交'):

        st.success('提交成功!', icon="✅")
