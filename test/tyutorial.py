import streamlit as st
import numpy as np
import pandas as pd


# タイトル
st.title('Streamlit 入門')

st.write('Dataframe')

df = pd.DataFrame({
    '1列目':[1,2,3,4,5],
    '2列目':[10,20,30,40,5]
})
# グラフ
st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=200,height=200)
st.table(df.style.highlight_max(axis=0))

# マークダウン記法
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
