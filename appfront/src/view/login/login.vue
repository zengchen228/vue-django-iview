<style lang="less">
  @import './login.less';
</style>

<template>
  <div class="login">
    <div class="login-con">
      <Card icon="log-in" title="欢迎登录" :bordered="false">
        <div class="form-con">
          <login-form @on-success-valid="handleSubmit"></login-form>
          <p class="login-tip">输入任意用户名和密码即可</p>
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
import LoginForm from '../../components/login-form'
import { mapActions } from 'vuex'
export default {
  components: {
    LoginForm
  },
  methods: {
    ...mapActions([
      'handleLogin'
    ]),
    handleSubmit ({ userName, password }) {
      this.handleLogin({ userName, password }).then(res => {
        if (res.stat === 'success') {
          this.$router.push({
            name: 'home'
          })
        } else {
          this.$Notice.error({title: res.msg})
        }
      })
    }
  },
  mounted: function () { // 登录清除上次的localStorage
    var storage = window.localStorage
    storage.clear()
  }
}
</script>

<style>

</style>
